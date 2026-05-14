import java.util.*;

public class InfixToPostfix {

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

        Stack<Character> stack = new Stack<>();

        String result = "";

        for (int i = 0; i < exp.length(); i++) {

            char ch = exp.charAt(i);

            if (Character.isLetterOrDigit(ch)) {
                result += ch;
            }

            else if (ch == '(') {
                stack.push(ch);
            }

            else if (ch == ')') {

                while (!stack.isEmpty() &&
                        stack.peek() != '(') {

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

        System.out.println("Postfix Expression: " + result);
    }
}