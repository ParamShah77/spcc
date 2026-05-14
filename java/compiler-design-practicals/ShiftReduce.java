import java.util.*;

public class ShiftReduce {

    public static void main(String[] args) {

        Scanner sc = new Scanner(System.in);

        System.out.print("Enter input string: ");

        String input = sc.next() + "$";

        Stack<String> stack = new Stack<>();

        int i = 0;

        while (i < input.length()) {

            String symbol = String.valueOf(input.charAt(i));

            stack.push(symbol);

            System.out.println(
                    "Shift: " + symbol);

            i++;

            boolean reduced = true;

            while (reduced) {

                reduced = false;

                if (stack.size() >= 2) {

                    String b = stack.pop();
                    String a = stack.pop();

                    if (a.equals("i")
                            && b.equals("d")) {

                        stack.push("E");

                        System.out.println(
                                "Reduce: id -> E");

                        reduced = true;
                    }

                    else {

                        stack.push(a);
                        stack.push(b);
                    }
                }

                if (stack.size() >= 3) {

                    String c = stack.pop();
                    String b = stack.pop();
                    String a = stack.pop();

                    if (a.equals("E")
                            && b.equals("+")
                            && c.equals("E")) {

                        stack.push("E");

                        System.out.println(
                                "Reduce: E+E -> E");

                        reduced = true;
                    }

                    else {

                        stack.push(a);
                        stack.push(b);
                        stack.push(c);
                    }
                }
            }

            System.out.println("Stack: " + stack);
        }

        if (stack.size() == 2
                && stack.get(0).equals("E")
                && stack.get(1).equals("$")) {

            System.out.println("String Accepted");
        }

        else {

            System.out.println("String Rejected");
        }
    }
}