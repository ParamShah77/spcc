import java.util.*;

public class InfixToPrefix {

    static int precedence(char ch) {

        switch(ch) {

            case '+':
            case '-':
                return 1;

            case '*':
            case '/':
                return 2;

            case '^':
                return 3;
        }

        return -1;
    }

    public static void main(String[] args) {

        Scanner sc = new Scanner(System.in);

        System.out.print("Enter infix expression: ");
        String exp = sc.next();

        StringBuilder input =
                new StringBuilder(exp);

        input.reverse();

        for (int i = 0; i < input.length(); i++) {

            if (input.charAt(i) == '(')
                input.setCharAt(i, ')');

            else if (input.charAt(i) == ')')
                input.setCharAt(i, '(');
        }

        Stack<Character> stack = new Stack<>();

        String result = "";

        for (int i = 0; i < input.length(); i++) {

            char ch = input.charAt(i);

            if (Character.isLetterOrDigit(ch)) {
                result += ch;
            }

            else if (ch == '(') {
                stack.push(ch);
            }

            else if (ch == ')') {

                while (!stack.isEmpty()
                        && stack.peek() != '(') {

                    result += stack.pop();
                }

                stack.pop();
            }

            else {

                while (!stack.isEmpty() &&
                        precedence(ch)
                        <= precedence(stack.peek())) {

                    result += stack.pop();
                }

                stack.push(ch);
            }
        }

        while (!stack.isEmpty()) {
            result += stack.pop();
        }

        StringBuilder prefix =
                new StringBuilder(result);

        System.out.println(
                "Prefix Expression: "
                        + prefix.reverse());
    }
}