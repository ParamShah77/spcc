"""
EXPERIMENT 1: LEXICAL ANALYSER
Scans source code and classifies tokens into categories.
Modify KEYWORDS set as per exam question.
"""

KEYWORDS   = {'int', 'float', 'if', 'else', 'while', 'for', 'return', 'switch', 'void', 'char', 'double'}
OPERATORS  = {'==', '!=', '<=', '>=', '++', '--', '+=', '-=', '+', '-', '*', '/', '=', '<', '>'}
PUNCTUATION = {'(', ')', '{', '}', '[', ']', ';', ',', '.'}


def lexer(code):
    tokens = []
    i = 0
    while i < len(code):
        # Skip whitespace
        if code[i].isspace():
            i += 1
            continue

        # Skip single-line comments
        if code[i:i+2] == '//':
            while i < len(code) and code[i] != '\n':
                i += 1
            continue

        # Skip multi-line comments
        if code[i:i+2] == '/*':
            i += 2
            while i < len(code) - 1 and code[i:i+2] != '*/':
                i += 1
            i += 2
            continue

        # Identifier or Keyword
        if code[i].isalpha() or code[i] == '_':
            j = i
            while j < len(code) and (code[j].isalnum() or code[j] == '_'):
                j += 1
            word = code[i:j]
            tok = 'KEYWORD' if word in KEYWORDS else 'IDENTIFIER'
            tokens.append((tok, word))
            i = j

        # Number (integer or float)
        elif code[i].isdigit():
            j = i
            while j < len(code) and (code[j].isdigit() or code[j] == '.'):
                j += 1
            tokens.append(('NUMBER', code[i:j]))
            i = j

        # String literal
        elif code[i] == '"':
            j = i + 1
            while j < len(code) and code[j] != '"':
                j += 1
            tokens.append(('STRING', code[i:j+1]))
            i = j + 1

        # Character literal
        elif code[i] == "'":
            j = i + 1
            while j < len(code) and code[j] != "'":
                j += 1
            tokens.append(('CHAR_LITERAL', code[i:j+1]))
            i = j + 1

        # Two-character operators (must check before single-char)
        elif code[i:i+2] in OPERATORS:
            tokens.append(('OPERATOR', code[i:i+2]))
            i += 2

        # Single-character operators
        elif code[i] in OPERATORS:
            tokens.append(('OPERATOR', code[i]))
            i += 1

        # Punctuation
        elif code[i] in PUNCTUATION:
            tokens.append(('PUNCTUATION', code[i]))
            i += 1

        # Unknown character
        else:
            tokens.append(('UNKNOWN', code[i]))
            i += 1

    return tokens


def display_tokens(tokens):
    print(f"\n{'TOKEN TYPE':<18} {'LEXEME'}")
    print("-" * 40)
    for typ, val in tokens:
        print(f"{typ:<18} {val}")
    print("-" * 40)
    print(f"Total tokens: {len(tokens)}")


# --- Test --------------------------------------------------------------------
if __name__ == "__main__":
    code = """
int main() {
    int x = 10;
    float y = 3.14;
    // this is a comment
    if (x > 5) {
        return x;
    }
    while (x != 0) {
        x--;
    }
}
"""
    print("Source Code:")
    print(code)
    tokens = lexer(code)
    display_tokens(tokens)
