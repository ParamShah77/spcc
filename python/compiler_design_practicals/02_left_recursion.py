"""
EXPERIMENT 2: LEFT RECURSION REMOVAL
Converts a left-recursive grammar to a non-left-recursive equivalent.

Left recursion form : A -> A α | β
After removal       : A -> β A'
                      A' -> α A' | eps

EXAM TIP: Change the `grammar` dict at the bottom as per your question.
Each production is a string where each character = one grammar symbol.
"""


def remove_left_recursion(grammar):
    """
    grammar: dict { NonTerminal: [list of production strings] }
    Returns a new grammar with immediate left recursion removed.
    """
    result = {}
    for A, prods in grammar.items():
        alpha = []  # productions that START with A  (left-recursive)
        beta  = []  # productions that DON'T start with A

        for p in prods:
            if p and p[0] == A:
                alpha.append(p[1:])   # strip the leading A
            else:
                beta.append(p)

        if not alpha:
            # No left recursion for this non-terminal -- keep as is
            result[A] = prods
        else:
            A1 = A + "'"          # new non-terminal  e.g. E -> E'
            # A  -> β A'  for every β
            result[A] = [b + A1 for b in beta]
            # A' -> α A' | eps
            result[A1] = [a + A1 for a in alpha] + ['eps']

    return result


def print_grammar(g, title="Grammar"):
    print(f"\n{'=' * 45}")
    print(f"  {title}")
    print('=' * 45)
    for nt, prods in g.items():
        print(f"  {nt}  ->  {' | '.join(prods)}")


# --- Example 1: Classic Expression Grammar -----------------------------------
# E -> E+T | T
# T -> T*F | F
# F -> (E) | i      ('i' represents 'id')
grammar1 = {
    'E': ['E+T', 'T'],
    'T': ['T*F', 'F'],
    'F': ['(E)', 'i'],
}

# --- Example 2: Simple left-recursive grammar --------------------------------
# A -> Aa | Ab | c | d
grammar2 = {
    'A': ['Aa', 'Ab', 'c', 'd'],
}

# --- Example 3: Multiple left-recursive non-terminals ------------------------
# S -> Sa | b
# T -> Tc | Td | e
grammar3 = {
    'S': ['Sa', 'b'],
    'T': ['Tc', 'Td', 'e'],
}


if __name__ == "__main__":
    for i, g in enumerate([grammar1, grammar2, grammar3], 1):
        print_grammar(g, f"Example {i} -- Original Grammar")
        new_g = remove_left_recursion(g)
        print_grammar(new_g, f"Example {i} -- After Left Recursion Removal")
        print()
