import java.util.*;

public class PostfixEvaluation {

    public static void main(String[] args) {

        Scanner sc = new Scanner(System.in);

        System.out.print("Enter postfix expression: ");
        String exp = sc.next();

        Stack<Integer> stack = new Stack<>();

        for (int i = 0; i < exp.length(); i++) {

            char ch = exp.charAt(i);

            if (Character.isDigit(ch)) {

                stack.push(ch - '0');
            }

            else {

                int b = stack.pop();
                int a = stack.pop();

                switch(ch) {

                    case '+':
                        stack.push(a + b);
                        break;

                    case '-':
                        stack.push(a - b);
                        break;

                    case '*':
                        stack.push(a * b);
                        break;

                    case '/':
                        stack.push(a / b);
                        break;
                }
            }
        }

        System.out.println(
                "Result = " + stack.pop());
    }
}