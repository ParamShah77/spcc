"""
EXPERIMENT 6: INTERMEDIATE CODE GENERATION
Converts an infix expression to postfix, then generates:
  - Quadruples : (op, arg1, arg2, result)
  - Triples    : (op, arg1, arg2)  -- result referenced by index

EXAM TIP:
  - If given POSTFIX directly -> skip infix_to_postfix(), call to_quads()/to_triples() directly.
  - If given INFIX -> call infix_to_postfix() first.
  - Multi-character operands (like 'ab') won't work with single-char parsing;
    use single chars to represent variables (a, b, c ...).
"""


def infix_to_postfix(expr):
    """
    Convert infix expression to postfix using operator precedence.
    Supports: + - * / ^ ( )
    Operands: single alphanumeric characters.
    """
    precedence = {'+': 1, '-': 1, '*': 2, '/': 2, '^': 3}
    output = []
    stack  = []

    for ch in expr:
        if ch == ' ':
            continue
        elif ch.isalnum():
            output.append(ch)
        elif ch == '(':
            stack.append(ch)
        elif ch == ')':
            while stack and stack[-1] != '(':
                output.append(stack.pop())
            if stack:
                stack.pop()   # discard '('
        else:
            # operator
            while (stack and stack[-1] != '(' and
                   precedence.get(stack[-1], 0) >= precedence.get(ch, 0)):
                output.append(stack.pop())
            stack.append(ch)

    while stack:
        output.append(stack.pop())

    return ''.join(output)


def to_quadruples(postfix):
    """
    Generate Quadruples from postfix expression.
    Returns list of (op, arg1, arg2, result) tuples.
    """
    operators = set('+-*/^')
    stack     = []
    quads     = []
    temp_num  = 1

    for ch in postfix:
        if ch not in operators:
            stack.append(ch)
        else:
            arg2 = stack.pop()
            arg1 = stack.pop()
            result = f"t{temp_num}"
            temp_num += 1
            quads.append((ch, arg1, arg2, result))
            stack.append(result)

    return quads


def to_triples(postfix):
    """
    Generate Triples from postfix expression.
    Returns list of (op, arg1, arg2) tuples.
    Result of instruction i is referenced as (i).
    """
    operators = set('+-*/^')
    stack     = []
    trips     = []

    for ch in postfix:
        if ch not in operators:
            stack.append(ch)
        else:
            arg2 = stack.pop()
            arg1 = stack.pop()
            trips.append((ch, arg1, arg2))
            stack.append(f"({len(trips) - 1})")   # reference by index

    return trips


def infix_to_prefix(expr):
    """Convert infix to prefix (reverse + postfix on reversed + reverse result)."""
    rev = expr[::-1].replace('(', '#').replace(')', '(').replace('#', ')')
    post = infix_to_postfix(rev)
    return post[::-1]


def display_quads(quads):
    print(f"\n{'-' * 45}")
    print("  QUADRUPLES")
    print(f"{'-' * 45}")
    print(f"  {'#':<5} {'OP':<6} {'ARG1':<10} {'ARG2':<10} RESULT")
    print(f"  {'-' * 40}")
    for i, (op, a1, a2, res) in enumerate(quads):
        print(f"  {i:<5} {op:<6} {a1:<10} {a2:<10} {res}")


def display_triples(trips):
    print(f"\n{'-' * 40}")
    print("  TRIPLES")
    print(f"{'-' * 40}")
    print(f"  {'#':<5} {'OP':<6} {'ARG1':<12} ARG2")
    print(f"  {'-' * 35}")
    for i, (op, a1, a2) in enumerate(trips):
        print(f"  {i:<5} {op:<6} {a1:<12} {a2}")


# --- Tests -------------------------------------------------------------------
if __name__ == "__main__":
    test_exprs = [
        "a+b*c-d",
        "(a+b)*(c-d)",
        "a*b+c*d",
        "a+b*c+d",
    ]

    for expr in test_exprs:
        postfix = infix_to_postfix(expr)
        prefix  = infix_to_prefix(expr)

        print(f"\n{'=' * 55}")
        print(f"  Infix  : {expr}")
        print(f"  Postfix: {postfix}")
        print(f"  Prefix : {prefix}")

        display_quads(to_quadruples(postfix))
        display_triples(to_triples(postfix))
