"""
EXPERIMENT 10: LOADER / LINKER
Two parts:

PART A -- D & R Records + Local Symbol Table
  Given a .asm file with EXTDEF and EXTREF directives:
    D record: external definitions (symbols this module exports + their addresses)
    R record: external references (symbols this module needs from outside)
    Local Symbol Table: subset of D-record symbols with their addresses

PART B -- Program Block Table
  Identifies USE blocks and builds a BLOCK table showing block name,
  starting address, and length.

All instructions assumed = 3 bytes.

EXAM TIP: Replace the `program` string with the one from your exam.
"""


# ==============================================================================
# PART A -- D & R Records
# ==============================================================================

INSTRUCTION_MNEMONICS = {
    'ADD', 'AND', 'COMP', 'DIV', 'J', 'JEQ', 'JGT', 'JLT',
    'JSUB', 'LDA', 'LDCH', 'LDB', 'LDL', 'LDX', 'MUL',
    'OR', 'RD', 'RSUB', 'STA', 'STCH', 'STB', 'STL',
    'STX', 'SUB', 'TD', 'TIX', 'WD',
}


def parse_line_dr(raw):
    """Return (label, mnemonic, operand) treating first token as label if not a mnemonic."""
    ALL_KNOWN = INSTRUCTION_MNEMONICS | {
        'START', 'END', 'BYTE', 'WORD', 'RESB', 'RESW',
        'BASE', 'EQU', 'EXTDEF', 'EXTREF', 'USE',
    }
    parts = raw.split()
    if not parts:
        return None, None, ''
    if parts[0].upper() not in ALL_KNOWN:
        label    = parts[0]
        mnemonic = parts[1].upper() if len(parts) > 1 else ''
        operand  = ' '.join(parts[2:]) if len(parts) > 2 else ''
    else:
        label    = None
        mnemonic = parts[0].upper()
        operand  = ' '.join(parts[1:]) if len(parts) > 1 else ''
    return label, mnemonic, operand


def generate_dr_records(program_text):
    """
    Simulate PASS 1 to find symbol addresses, then emit D and R records.
    """
    lines = [l for l in program_text.strip().splitlines() if l.strip()]

    symbol_table = {}   # ALL local labels -> address
    extdef_list  = []   # symbols this module exports (EXTDEF)
    extref_list  = []   # symbols this module needs   (EXTREF)
    locctr       = 0
    start_addr   = 0

    for raw in lines:
        label, mnem, operand = parse_line_dr(raw)

        if mnem == 'START':
            try:
                start_addr = int(operand.split()[0], 16)
            except (ValueError, IndexError):
                start_addr = 0
            locctr = start_addr
            continue

        if mnem == 'END':
            break

        if mnem == 'EXTDEF':
            extdef_list = [s.strip() for s in operand.replace(',', ' ').split()]
            continue

        if mnem == 'EXTREF':
            extref_list = [s.strip() for s in operand.replace(',', ' ').split()]
            continue

        # Record label
        if label:
            symbol_table[label] = locctr

        # Advance LOCCTR
        if mnem == 'RESW':
            try: locctr += 3 * int(operand)
            except ValueError: locctr += 3
        elif mnem == 'RESB':
            try: locctr += int(operand)
            except ValueError: locctr += 1
        elif mnem == 'WORD':
            locctr += 3
        elif mnem == 'BYTE':
            op = operand.strip()
            if op.upper().startswith("C'"):
                locctr += len(op) - 3
            elif op.upper().startswith("X'"):
                locctr += (len(op) - 3 + 1) // 2
            else:
                locctr += 1
        elif mnem in ('BASE', 'EQU', 'USE'):
            pass
        else:
            locctr += 3   # default: 3 bytes per instruction

    # --- Build records --------------------------------------------------------
    # D record format: D^ sym^addr ^ sym^addr ...
    d_parts = []
    for sym in extdef_list:
        addr = symbol_table.get(sym, 0)
        d_parts.append(f"{sym}^{addr:06d}")
    d_record = "D^ " + "^".join(d_parts) if d_parts else "D^"

    # R record format: R^ sym ^ sym ^
    r_parts = [f" {sym} ^" for sym in extref_list]
    r_record = "R^" + "".join(r_parts) if r_parts else "R^"

    # --- Display -------------------------------------------------------------
    print(f"\n{'=' * 50}")
    print("  PART A -- D & R Records")
    print(f"{'=' * 50}")
    print(f"\n  D Record (External Definitions):")
    print(f"  {d_record}")
    print(f"\n  R Record (External References):")
    print(f"  {r_record}")

    print(f"\n{'-' * 40}")
    print("  Local Symbol Table")
    print(f"{'-' * 40}")
    print(f"  {'Symbol NAME':<15} value")
    print(f"  {'-' * 28}")
    for sym in extdef_list:
        if sym in symbol_table:
            print(f"  {sym:<15} {symbol_table[sym]:06d}")

    return d_record, r_record, symbol_table


# ==============================================================================
# PART B -- Program Block Table
# ==============================================================================

def generate_block_table(program_text):
    """
    Identify USE blocks and generate the Program Block Table.
    Each USE <name> starts a new block; USE with no name returns to default.
    """
    lines = [l for l in program_text.strip().splitlines() if l.strip()]

    blocks         = {}          # block_name -> {'start': addr, 'locctr': addr}
    current_block  = 'DEFAULT'
    global_locctr  = 0
    start_addr     = 0

    blocks[current_block] = {'start': 0, 'locctr': 0}

    for raw in lines:
        label, mnem, operand = parse_line_dr(raw)

        if mnem == 'START':
            try: start_addr = int(operand.split()[0], 16)
            except (ValueError, IndexError): start_addr = 0
            global_locctr = start_addr
            blocks[current_block]['start'] = start_addr
            blocks[current_block]['locctr'] = start_addr
            continue

        if mnem == 'END':
            break

        if mnem == 'USE':
            new_block = operand.strip() if operand.strip() else 'DEFAULT'
            if new_block not in blocks:
                blocks[new_block] = {'start': blocks[current_block]['locctr'], 'locctr': blocks[current_block]['locctr']}
            current_block = new_block
            continue

        if mnem in ('EXTDEF', 'EXTREF', 'BASE', 'EQU'):
            continue

        # Advance this block's LOCCTR
        blk = blocks[current_block]
        if mnem == 'RESW':
            try: blk['locctr'] += 3 * int(operand)
            except ValueError: blk['locctr'] += 3
        elif mnem == 'RESB':
            try: blk['locctr'] += int(operand)
            except ValueError: blk['locctr'] += 1
        elif mnem == 'WORD':
            blk['locctr'] += 3
        elif mnem == 'BYTE':
            op = operand.strip()
            if op.upper().startswith("C'"):
                blk['locctr'] += len(op) - 3
            elif op.upper().startswith("X'"):
                blk['locctr'] += (len(op) - 3 + 1) // 2
            else:
                blk['locctr'] += 1
        else:
            blk['locctr'] += 3

    # --- Display -------------------------------------------------------------
    print(f"\n{'=' * 55}")
    print("  PART B -- Program Block Table")
    print(f"{'=' * 55}")
    print(f"  {'Block Name':<15} {'Start Address':<18} {'Length (bytes)'}")
    print(f"  {'-' * 50}")
    for bname, binfo in blocks.items():
        length = binfo['locctr'] - binfo['start']
        print(f"  {bname:<15} {binfo['start']:06X}h   ({binfo['start']:>6})   {length}")


# --- Exam Sample (from guideline) ---------------------------------------------
program_dr = """
PG1 START 0000
    EXTDEF A, B
    EXTREF C, D
    ADD ABC
A   SUB PQR
    ADD ABC1
B   MUL ABC
    END
"""

# Expected output:
#   D^ A^000003^B^000009
#   R^ C ^ D ^
#
#   Local Symbol Table
#   A   000003
#   B   000009

# --- Sample with USE blocks ---------------------------------------------------
program_blocks = """
PROGA START  0000
FIRST LDA    ALPHA
      USE    CDATA
      LDX    BETA
      USE    CBLKS
ALPHA RESW   1
      USE
BETA  RESW   1
      END    FIRST
"""

if __name__ == "__main__":
    print("=" * 60)
    print("  EXAM SAMPLE -- D & R Records (from guideline)")
    print("=" * 60)
    generate_dr_records(program_dr)

    print("\n" + "=" * 60)
    print("  SAMPLE -- Program Block Table (USE blocks)")
    print("=" * 60)
    generate_block_table(program_blocks)
