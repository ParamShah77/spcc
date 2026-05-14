"""
EXPERIMENT 5: LR(1) PARSER SIMULATION
Bottom-up shift-reduce parser using ACTION and GOTO tables.

EXAM PROCESS:
  1. On paper: build LR(0)/SLR/CLR items -> fill ACTION & GOTO tables.
  2. Hardcode the tables here -> run simulation.

Grammar:
  0: S'-> E
  1: E -> E + T
  2: E -> T
  3: T -> T * F
  4: T -> F
  5: F -> ( E )
  6: F -> id

Tokens must be space-separated: "id + id * id"

EXAM TIP: Replace ACTION, GOTO, RULES as per your grammar.
"""

# (LHS non-terminal, length of RHS)
RULES = [
    ('S', 1),   # 0: S' -> E
    ('E', 3),   # 1: E  -> E + T
    ('E', 1),   # 2: E  -> T
    ('T', 3),   # 3: T  -> T * F
    ('T', 1),   # 4: T  -> F
    ('F', 3),   # 5: F  -> ( E )
    ('F', 1),   # 6: F  -> id
]

# 's' = shift, 'r' = reduce, 'acc' = accept
ACTION = {
    0:  {'id': ('s', 5), '(':  ('s', 4)},
    1:  {'+':  ('s', 6), '$':  'acc'},
    2:  {'+':  ('r', 2), '*':  ('s', 7), ')': ('r', 2), '$': ('r', 2)},
    3:  {'+':  ('r', 4), '*':  ('r', 4), ')': ('r', 4), '$': ('r', 4)},
    4:  {'id': ('s', 5), '(':  ('s', 4)},
    5:  {'+':  ('r', 6), '*':  ('r', 6), ')': ('r', 6), '$': ('r', 6)},
    6:  {'id': ('s', 5), '(':  ('s', 4)},
    7:  {'id': ('s', 5), '(':  ('s', 4)},
    8:  {'+':  ('s', 6), ')':  ('s', 11)},
    9:  {'+':  ('r', 1), '*':  ('s', 7), ')': ('r', 1), '$': ('r', 1)},
    10: {'+':  ('r', 3), '*':  ('r', 3), ')': ('r', 3), '$': ('r', 3)},
    11: {'+':  ('r', 5), '*':  ('r', 5), ')': ('r', 5), '$': ('r', 5)},
}

GOTO = {
    0: {'E': 1, 'T': 2,  'F': 3},
    4: {'E': 8, 'T': 2,  'F': 3},
    6: {        'T': 9,  'F': 3},
    7: {                 'F': 10},
}


def lr_parse(tokens_str):
    """
    Simulate LR parsing.
    tokens_str: space-separated token string, e.g. "id + id * id"
    """
    tokens = tokens_str.split() + ['$']
    stack  = [0]          # stack holds alternating: state, symbol, state, symbol ...
    i = 0

    print(f"\n{'-' * 75}")
    print(f"  Input: {tokens_str}")
    print(f"{'-' * 75}")
    print(f"{'STACK':<35} {'REMAINING INPUT':<25} ACTION")
    print(f"{'-' * 75}")

    while True:
        state = stack[-1]
        tok   = tokens[i]

        stack_display = str(stack)
        remaining     = ' '.join(tokens[i:])
        print(f"{stack_display:<35} {remaining:<25}", end='')

        action = ACTION.get(state, {}).get(tok)

        if action is None:
            print(f"ERROR -- no action for state {state}, token '{tok}'")
            return False

        if action == 'acc':
            print("ACCEPT OK")
            return True

        kind, num = action

        if kind == 's':
            print(f"Shift  -> go to state {num}")
            stack.append(tok)
            stack.append(num)
            i += 1

        elif kind == 'r':
            lhs, rlen = RULES[num]
            # Pop 2 * rlen items (symbol + state per symbol)
            for _ in range(rlen * 2):
                stack.pop()
            top_state = stack[-1]
            goto_state = GOTO.get(top_state, {}).get(lhs)
            if goto_state is None:
                print(f"ERROR -- no GOTO for state {top_state}, symbol '{lhs}'")
                return False
            stack.append(lhs)
            stack.append(goto_state)
            rhs_repr = {0:"E", 1:"E+T", 2:"T", 3:"T*F", 4:"F", 5:"(E)", 6:"id"}.get(num, "?")
            print(f"Reduce {num}: {lhs} -> {rhs_repr}")


# --- Test Cases --------------------------------------------------------------
if __name__ == "__main__":
    tests = [
        ("id + id * id", True),
        ("id * id",      True),
        ("( id + id )",  True),
        ("id + * id",    False),
    ]

    for inp, expected in tests:
        result = lr_parse(inp)
        status = "OK PASS" if result == expected else "FAIL FAIL"
        print(f"  Result: {'ACCEPTED' if result else 'REJECTED'}  [{status}]\n")
