"""
EXPERIMENT 8: ASSEMBLER (Two-Pass Simulation)
Generates:
  - Symbol Table  (label -> address)
  - H Record      H^ProgName^StartAddr^ProgLength
  - E Record      E^FirstExecutableAddr

Assumptions:
  - Every regular instruction = 3 bytes.
  - RESW n  = 3n bytes,  RESB n = n bytes.
  - BYTE C'xyz' = len(xyz) bytes,  BYTE X'hex' = (hex digits)/2 bytes.
  - BASE, EQU directives consume 0 bytes.

EXAM TIP: Replace `program` string with the one given in your exam.
"""

# Instruction mnemonics (subset of SIC); anything in this set = 3 bytes
OPTAB = {
    'ADD', 'AND', 'COMP', 'DIV', 'J', 'JEQ', 'JGT', 'JLT',
    'JSUB', 'LDA', 'LDCH', 'LDB', 'LDL', 'LDS', 'LDT', 'LDX',
    'MUL', 'OR', 'RD', 'RSUB', 'STA', 'STCH', 'STB', 'STL',
    'STS', 'STT', 'STX', 'SUB', 'TD', 'TIX', 'WD',
}

DIRECTIVES_NO_SPACE = {'BASE', 'EQU', 'NOBASE'}


def byte_size(operand):
    """Return byte count for a BYTE directive operand."""
    op = operand.strip()
    if op.upper().startswith("C'") and op.endswith("'"):
        return len(op) - 3          # C'EOF' -> 3
    if op.upper().startswith("X'") and op.endswith("'"):
        hex_digits = len(op) - 3
        return (hex_digits + 1) // 2
    return 1                        # fallback


def parse_fields(raw):
    """
    Split a line into (label, mnemonic, operand).
    First token is a label if it is NOT a known mnemonic/directive.
    """
    ALL_MNEMONICS = OPTAB | {'START', 'END', 'BYTE', 'WORD', 'RESB', 'RESW',
                              'BASE', 'EQU', 'NOBASE', 'EXTDEF', 'EXTREF', 'USE'}
    parts = raw.split()
    if not parts:
        return None, None, None

    if parts[0].upper().lstrip('+') not in ALL_MNEMONICS:
        label    = parts[0]
        mnemonic = parts[1].upper() if len(parts) > 1 else ''
        operand  = parts[2]         if len(parts) > 2 else ''
    else:
        label    = None
        mnemonic = parts[0].upper().lstrip('+')
        operand  = parts[1]         if len(parts) > 1 else ''

    return label, mnemonic, operand


def two_pass_assemble(program_text):
    lines = [l for l in program_text.strip().splitlines() if l.strip()]

    symbol_table = {}
    locctr       = 0
    start_addr   = 0
    prog_name    = 'PROG'
    first_exec   = 0

    # === PASS 1: Build Symbol Table ==========================================
    for raw in lines:
        label, mnem, operand = parse_fields(raw)

        if mnem == 'START':
            prog_name  = label if label else 'PROG'
            start_addr = int(operand, 16) if operand else 0
            locctr     = start_addr
            first_exec = start_addr
            continue

        if mnem == 'END':
            # operand of END = first executable instruction label
            if operand and operand in symbol_table:
                first_exec = symbol_table[operand]
            break

        # Record label
        if label:
            if label in symbol_table:
                print(f"  WARNING: duplicate label '{label}' -- overwriting.")
            symbol_table[label] = locctr

        # Advance LOCCTR
        if mnem in DIRECTIVES_NO_SPACE:
            pass                                # 0 bytes
        elif mnem == 'WORD':
            locctr += 3
        elif mnem == 'RESW':
            locctr += 3 * int(operand) if operand else 0
        elif mnem == 'RESB':
            locctr += int(operand) if operand else 0
        elif mnem == 'BYTE':
            locctr += byte_size(operand)
        elif mnem in OPTAB or mnem.lstrip('+') in OPTAB:
            locctr += 3                         # Format 3 (exam default)
        else:
            locctr += 3                         # unknown -> assume 3 bytes

    prog_length = locctr - start_addr

    # === PASS 2: Print Results ===============================================
    print(f"\n{'=' * 50}")
    print("  SYMBOL TABLE")
    print(f"{'=' * 50}")
    print(f"  {'Label':<15} {'Address (Hex)'}")
    print(f"  {'-' * 30}")
    for sym, addr in symbol_table.items():
        print(f"  {sym:<15} {addr:06X}")

    print(f"\n{'=' * 50}")
    print("  OBJECT PROGRAM RECORDS")
    print(f"{'=' * 50}")
    print(f"  H Record: H^{prog_name:<6}^{start_addr:06X}^{prog_length:06X}")
    print(f"  E Record: E^{first_exec:06X}")
    print(f"\n  Program Name  : {prog_name}")
    print(f"  Start Address : {start_addr:06X}h")
    print(f"  Program Length: {prog_length:06X}h  ({prog_length} bytes)")

    return symbol_table, prog_name, start_addr, prog_length, first_exec


# --- Sample Program -----------------------------------------------------------
program = """
COPY   START  0000
FIRST  STL    RETADR
       LDB    LENGTH
       BASE   LENGTH
LOOP   JSUB   RDREC
       LDA    LENGTH
       COMP   ZERO
       JEQ    ENDFIL
       JSUB   WRREC
       J      LOOP
ENDFIL LDA    EOF
       STA    BUFFER
       LDA    THREE
       STA    LENGTH
       JSUB   WRREC
       RSUB
EOF    BYTE   C'EOF'
THREE  WORD   3
ZERO   WORD   0
RETADR RESW   1
LENGTH RESW   1
BUFFER RESB   4096
       END    FIRST
"""

if __name__ == "__main__":
    two_pass_assemble(program)
