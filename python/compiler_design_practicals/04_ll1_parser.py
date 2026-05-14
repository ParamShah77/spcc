"""
EXPERIMENT 4: LL(1) PARSER SIMULATION
Top-down predictive parser using a stack.

EXAM PROCESS:
  1. On paper: compute FIRST/FOLLOW -> build LL(1) table.
  2. Hardcode the table here -> run simulation.

Grammar (single-char symbols, e=E', t=T', i=id):
  E  -> T e
  e  -> + T e | eps
  T  -> F t
  t  -> * F t | eps
  F  -> ( E ) | i

EXAM TIP: Change `TABLE` and `test_inputs` as per your question.
"""

# --- Parsing Table ------------------------------------------------------------
# table[NonTerminal][terminal] = production string  (or 'eps')
TABLE = {
    'E': {'i': 'Te',  '(': 'Te'},
    'e': {'+': '+Te', ')': 'eps', '$': 'eps'},
    'T': {'i': 'Ft',  '(': 'Ft'},
    't': {'+': 'eps',   '*': '*Ft', ')': 'eps', '$': 'eps'},
    'F': {'i': 'i',   '(': '(E)'},
}

START = 'E'


def ll1_parse(table, start, inp):
    """
    Simulate LL(1) parsing.
    inp: input string of single-char terminals (e.g. "i+i*i")
    Returns True if accepted, False otherwise.
    """
    stack = ['$', start]   # bottom is left, top is right
    inp_full = inp + '$'
    i = 0

    print(f"\n{'-' * 70}")
    print(f"  Input: {inp}")
    print(f"{'-' * 70}")
    print(f"{'STACK':<30} {'REMAINING INPUT':<22} ACTION")
    print(f"{'-' * 70}")

    while stack:
        top = stack[-1]
        cur = inp_full[i]

        stack_display = ' '.join(reversed(stack))
        remaining     = inp_full[i:]
        print(f"{stack_display:<30} {remaining:<22}", end='')

        # Accept condition
        if top == '$' and cur == '$':
            print("ACCEPT OK")
            return True

        # Match terminal
        elif top == cur:
            print(f"Match '{cur}'")
            stack.pop()
            i += 1

        # Apply production
        elif top in table:
            if cur in table[top]:
                prod = table[top][cur]
                print(f"{top} -> {prod}")
                stack.pop()
                if prod != 'eps':
                    for sym in reversed(prod):
                        stack.append(sym)
            else:
                print(f"ERROR -- no entry for ({top}, {cur})")
                return False

        else:
            print(f"ERROR -- unexpected symbol '{top}' on stack")
            return False

    print("ERROR -- stack empty without accepting")
    return False


# --- Test Cases --------------------------------------------------------------
if __name__ == "__main__":
    test_inputs = [
        ("i+i*i",   True),   # valid:  id + id * id
        ("i*i+i",   True),   # valid:  id * id + id
        ("(i+i)*i", True),   # valid:  (id+id)*id
        ("i+",      False),  # invalid
        ("i++i",    False),  # invalid
    ]

    for inp, expected in test_inputs:
        result = ll1_parse(TABLE, START, inp)
        status = "OK PASS" if result == expected else "FAIL FAIL"
        print(f"  Result: {'ACCEPTED' if result else 'REJECTED'}  [{status}]\n")
