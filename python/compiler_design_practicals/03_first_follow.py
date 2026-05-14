"""
EXPERIMENT 3: FIRST and FOLLOW Sets
Used to construct the LL(1) parsing table.

Each production is a LIST of symbol strings:
  grammar = {
      'E': [['T', 'e']],        # E -> T e
      'e': [['+', 'T', 'e'],    # e -> + T e
             ['eps']],          # e -> eps
  }

Non-terminals = keys of grammar dict.
Terminals     = any string NOT in grammar dict.
'eps'         = the empty (epsilon) production.

EXAM TIP: Change grammar dict and START as per your exam question.
"""

EPS = 'eps'


def compute_first(grammar):
    first = {nt: set() for nt in grammar}
    changed = True
    while changed:
        changed = False
        for A, productions in grammar.items():
            for prod in productions:
                # Epsilon production
                if prod == [EPS]:
                    if EPS not in first[A]:
                        first[A].add(EPS)
                        changed = True
                    continue
                # Normal production: scan symbols left to right
                all_derive_eps = True
                for sym in prod:
                    if sym in grammar:
                        added = first[sym] - {EPS} - first[A]
                        if added:
                            first[A] |= added
                            changed = True
                        if EPS not in first[sym]:
                            all_derive_eps = False
                            break
                    else:
                        if sym not in first[A]:
                            first[A].add(sym)
                            changed = True
                        all_derive_eps = False
                        break
                if all_derive_eps and EPS not in first[A]:
                    first[A].add(EPS)
                    changed = True
    return first


def compute_follow(grammar, start, first):
    follow = {nt: set() for nt in grammar}
    follow[start].add('$')
    changed = True
    while changed:
        changed = False
        for A, productions in grammar.items():
            for prod in productions:
                if prod == [EPS]:
                    continue
                trailer = set(follow[A])
                for sym in reversed(prod):
                    if sym in grammar:
                        added = trailer - follow[sym]
                        if added:
                            follow[sym] |= added
                            changed = True
                        if EPS in first[sym]:
                            trailer = trailer | (first[sym] - {EPS})
                        else:
                            trailer = set(first[sym])
                    else:
                        trailer = {sym}
    return follow


def print_sets(first, follow):
    print()
    print("=" * 50)
    print("  FIRST Sets")
    print("=" * 50)
    for nt, items in first.items():
        vals = ", ".join(sorted(items))
        print(f"  FIRST({nt}) = {{ {vals} }}")
    print()
    print("=" * 50)
    print("  FOLLOW Sets")
    print("=" * 50)
    for nt, items in follow.items():
        vals = ", ".join(sorted(items))
        print(f"  FOLLOW({nt}) = {{ {vals} }}")


# ---------------------------------------------------------------------------
# Grammar (after left-recursion removal):
# E  -> T e      (e = E prime)
# e  -> + T e | eps
# T  -> F t      (t = T prime)
# t  -> * F t | eps
# F  -> ( E ) | i
# ---------------------------------------------------------------------------
grammar = {
    "E": [["T", "e"]],
    "e": [["+", "T", "e"], [EPS]],
    "T": [["F", "t"]],
    "t": [["*", "F", "t"], [EPS]],
    "F": [["(", "E", ")"], ["i"]],
}
START = "E"

if __name__ == "__main__":
    first  = compute_first(grammar)
    follow = compute_follow(grammar, START, first)
    print_sets(first, follow)
    print()
    print("Expected:")
    print("  FIRST(E) = { (, i }       FIRST(e) = { +, eps }")
    print("  FIRST(T) = { (, i }       FIRST(t) = { *, eps }")
    print("  FIRST(F) = { (, i }")
    print("  FOLLOW(E) = { $, ) }     FOLLOW(e) = { $, ) }")
    print("  FOLLOW(T) = { $, ), + }  FOLLOW(t) = { $, ), + }")
    print("  FOLLOW(F) = { $, ), *, + }")
