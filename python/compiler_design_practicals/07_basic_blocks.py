"""
EXPERIMENT 7: BASIC BLOCK IDENTIFICATION FROM TAC
Given Three Address Code (TAC), identifies leaders and divides
code into basic blocks.

Leader Rules:
  1. First statement of the program.
  2. Any statement that is the TARGET of a jump (goto / if-goto).
  3. Any statement that immediately FOLLOWS a jump.

EXAM TIP: Change the `tac` list as per your question.
"""


def find_basic_blocks(tac):
    n = len(tac)
    leaders = {0}   # Rule 1: first statement is always a leader

    # Build a label -> line-index map
    label_map = {}
    for idx, stmt in enumerate(tac):
        stripped = stmt.strip()
        if ':' in stripped:
            label = stripped.split(':')[0].strip()
            label_map[label] = idx

    # Identify leaders from jumps
    for i, stmt in enumerate(tac):
        words = stmt.strip().split()
        if not words:
            continue

        lower = stmt.strip().lower()

        # Unconditional or conditional goto
        if 'goto' in lower:
            target_label = words[-1]   # last word is the label
            if target_label in label_map:
                leaders.add(label_map[target_label])   # Rule 2
            if i + 1 < n:
                leaders.add(i + 1)                     # Rule 3

    leaders_sorted = sorted(leaders)

    # Build blocks: from one leader up to (not including) the next
    blocks = []
    for k, start in enumerate(leaders_sorted):
        end = leaders_sorted[k + 1] if k + 1 < len(leaders_sorted) else n
        blocks.append((start, tac[start:end]))

    # --- Display -------------------------------------------------------------
    print(f"\n{'=' * 55}")
    print(f"  TAC Input ({n} statements)")
    print(f"{'=' * 55}")
    for i, s in enumerate(tac):
        print(f"  {i:>3}: {s}")

    print(f"\n  Leaders (line indices): {leaders_sorted}")
    print(f"  Total Basic Blocks    : {len(blocks)}\n")

    for blk_num, (start_line, stmts) in enumerate(blocks, 1):
        print(f"  --- Block {blk_num} (starts at line {start_line}) ---")
        for s in stmts:
            print(f"        {s}")
        print()

    return blocks


# --- Sample TAC 1 ------------------------------------------------------------
tac1 = [
    "t1 = a + b",
    "t2 = c - d",
    "if t1 > t2 goto L1",
    "t3 = t2 * e",
    "goto L2",
    "L1: t3 = t1 + e",
    "L2: t4 = t3 / f",
]

# --- Sample TAC 2 (loop) -----------------------------------------------------
tac2 = [
    "i = 1",
    "sum = 0",
    "L1: if i > 10 goto L2",
    "sum = sum + i",
    "i = i + 1",
    "goto L1",
    "L2: print sum",
]

if __name__ == "__main__":
    print("=" * 60)
    print("  EXAMPLE 1")
    print("=" * 60)
    find_basic_blocks(tac1)

    print("=" * 60)
    print("  EXAMPLE 2 -- Loop")
    print("=" * 60)
    find_basic_blocks(tac2)
