"""
EXPERIMENT 9: MACRO PROCESSOR
Given an .ASM file, generates:
  - DEFTAB  (Definition Table) -- stores macro body lines with index
  - NAMETAB (Name Table)       -- maps macro name -> starting DEFTAB index

Macro syntax:
  MacroName  MACRO  &param1, &param2, ...
             < body statements >
             MEND

EXAM TIP: Replace `asm_code` with the program given in your exam.
"""


def macro_processor(asm_code):
    DEFTAB  = []    # list of strings (one per line inside macro definitions)
    NAMETAB = {}    # {macro_name: start_index_in_DEFTAB}

    lines     = [l.rstrip() for l in asm_code.strip().splitlines()]
    in_macro  = False
    macro_name = None

    for line in lines:
        stripped = line.strip()
        if not stripped:
            continue

        parts = stripped.split()

        # Detect macro definition header:  Name  MACRO  [params]
        if len(parts) >= 2 and parts[1].upper() == 'MACRO':
            macro_name = parts[0]
            NAMETAB[macro_name] = len(DEFTAB)   # point to header row
            DEFTAB.append(stripped)              # store header line
            in_macro = True

        # Detect MEND
        elif parts[0].upper() == 'MEND':
            if in_macro:
                DEFTAB.append(stripped)
                in_macro = False
                macro_name = None

        # Body of macro
        elif in_macro:
            DEFTAB.append(stripped)

        # Regular code (not inside macro) -- just show it
        # else: pass  ← non-macro lines are expanded/passed through in real macro processors

    # --- Display -------------------------------------------------------------
    print(f"\n{'=' * 50}")
    print("  NAMETAB  (Macro Name Table)")
    print(f"{'=' * 50}")
    print(f"  {'Macro Name':<20} {'DEFTAB Start Index'}")
    print(f"  {'-' * 40}")
    for name, idx in NAMETAB.items():
        print(f"  {name:<20} {idx}")

    print(f"\n{'=' * 50}")
    print("  DEFTAB  (Macro Definition Table)")
    print(f"{'=' * 50}")
    print(f"  {'Index':<8} {'Line'}")
    print(f"  {'-' * 45}")
    for i, dline in enumerate(DEFTAB):
        print(f"  {i:<8} {dline}")

    return DEFTAB, NAMETAB


# --- Sample 1: Exam-style program ---------------------------------------------
asm_code1 = """
ADDL    MACRO  &A, &B
        LDA    &A
        ADD    &B
        STA    &A
        MEND
SUBL    MACRO  &X, &Y
        LDA    &X
        SUB    &Y
        STA    &X
        MEND
MAIN    START  0000
        ADDL   NUM1, NUM2
        SUBL   NUM3, NUM4
NUM1    RESW   1
NUM2    RESW   1
NUM3    RESW   1
NUM4    RESW   1
        END    MAIN
"""

# --- Sample 2: Single macro ---------------------------------------------------
asm_code2 = """
INCR    MACRO  &REG
        LDA    &REG
        ADD    ONE
        STA    &REG
        MEND
PROG    START  1000
        INCR   ALPHA
        INCR   BETA
ALPHA   RESW   1
BETA    RESW   1
ONE     WORD   1
        END    PROG
"""

if __name__ == "__main__":
    print("=" * 55)
    print("  EXAMPLE 1 -- Two Macros (ADDL and SUBL)")
    print("=" * 55)
    macro_processor(asm_code1)

    print("\n" + "=" * 55)
    print("  EXAMPLE 2 -- Single Macro (INCR)")
    print("=" * 55)
    macro_processor(asm_code2)
