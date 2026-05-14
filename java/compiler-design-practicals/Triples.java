import java.util.*;

public class Triples {

    public static void main(String[] args) {

        Scanner sc = new Scanner(System.in);

        System.out.print("Enter postfix expression: ");

        String postfix = sc.next();

        Stack<String> stack = new Stack<>();

        int index = 0;

        System.out.println("\nIndex\top\targ1\targ2");

        for (int i = 0; i < postfix.length(); i++) {

            char ch = postfix.charAt(i);

            // Operand
            if (Character.isLetterOrDigit(ch)) {

                stack.push(ch + "");
            }

            // Operator
            else {

                String b = stack.pop();
                String a = stack.pop();

                System.out.println(index
                        + "\t"
                        + ch
                        + "\t"
                        + a
                        + "\t"
                        + b);

                stack.push("(" + index + ")");

                index++;
            }
        }
    }
}