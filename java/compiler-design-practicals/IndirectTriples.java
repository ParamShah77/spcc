import java.util.*;

public class IndirectTriples {

    public static void main(String[] args) {

        Scanner sc = new Scanner(System.in);

        System.out.print("Enter postfix expression: ");

        String postfix = sc.next();

        Stack<String> stack = new Stack<>();

        ArrayList<String[]> triples =
                new ArrayList<>();

        int index = 0;

        // Generate triples
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

                triples.add(new String[] {
                        ch + "",
                        a,
                        b
                });

                stack.push("(" + index + ")");

                index++;
            }
        }

        // Print Triple Table
        System.out.println("\nTRIPLE TABLE");

        System.out.println(
                "Index\top\targ1\targ2");

        for (int i = 0; i < triples.size(); i++) {

            String row[] = triples.get(i);

            System.out.println(
                    i + "\t"
                            + row[0]
                            + "\t"
                            + row[1]
                            + "\t"
                            + row[2]);
        }

        // Print Pointer Table
        System.out.println("\nPOINTER TABLE");

        System.out.println(
                "Pointer\tTriple Index");

        for (int i = 0; i < triples.size(); i++) {

            System.out.println(
                    "P" + i
                            + "\t"
                            + i);
        }
    }
}