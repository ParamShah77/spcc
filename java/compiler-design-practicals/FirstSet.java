import java.util.*;

public class FirstSet {

    public static void main(String[] args) {

        Scanner sc = new Scanner(System.in);

        System.out.print("Enter production (Example A=aB|b): ");
        String prod = sc.next();

        char nonTerminal = prod.charAt(0);

        Set<Character> first = new HashSet<>();

        String rhs = prod.substring(2);

        String parts[] = rhs.split("\\|");

        for (String p : parts) {

            char firstChar = p.charAt(0);

            first.add(firstChar);
        }

        System.out.println("FIRST(" + nonTerminal + ") = " + first);
    }
}