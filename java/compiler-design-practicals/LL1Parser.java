import java.util.*;

public class LL1Parser {

    public static void main(String[] args) {

        Scanner sc = new Scanner(System.in);

        System.out.print("Enter input string: ");

        String input = sc.next() + "$";

        Stack<Character> stack = new Stack<>();

        stack.push('$');

        stack.push('S');

        int i = 0;

        while (!stack.isEmpty()) {

            char top = stack.peek();

            char current = input.charAt(i);

            System.out.println("Stack: " + stack +
                    " Input: " + input.substring(i));

            if (top == '$' && current == '$') {

                System.out.println("String Accepted");
                return;
            }

            else if (top == current) {

                stack.pop();
                i++;
            }

            else if (top == 'S' && current == 'a') {

                stack.pop();

                stack.push('b');
                stack.push('S');
                stack.push('a');

                System.out.println("S -> aSb");
            }

            else if (top == 'S' && current == 'b') {

                stack.pop();

                System.out.println("S -> ε");
            }

            else {

                System.out.println("String Rejected");
                return;
            }
        }
    }
}