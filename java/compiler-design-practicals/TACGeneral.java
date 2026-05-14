import java.util.*;

public class TACGeneral {

    public static void main(String[] args) {

        Scanner sc = new Scanner(System.in);

        System.out.print("Enter postfix expression: ");

        String postfix = sc.next();

        Stack<String> stack = new Stack<>();

        int temp = 1;

        System.out.println("\nThree Address Code:");

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

                String t = "T" + temp;

                System.out.println(
                        t + " = "
                                + a + " "
                                + ch + " "
                                + b);

                stack.push(t);

                temp++;
            }
        }
    }
}