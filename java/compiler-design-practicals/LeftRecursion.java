import java.util.*;

public class LeftRecursion {

    public static void main(String[] args) {

        Scanner sc = new Scanner(System.in);

        System.out.print("Enter production (Example A=Aa|b): ");
        String prod = sc.next();

        char nonTerminal = prod.charAt(0);

        String rhs = prod.substring(2);

        String parts[] = rhs.split("\\|");

        String alpha = "";
        String beta = "";

        for (String p : parts) {

            if (p.charAt(0) == nonTerminal) {
                alpha = p.substring(1);
            }

            else {
                beta = p;
            }
        }

        System.out.println("After removing left recursion:");

        System.out.println(nonTerminal + " -> " + beta + nonTerminal + "'");

        System.out.println(nonTerminal + "' -> " +
                alpha + nonTerminal + "' | ε");
    }
}