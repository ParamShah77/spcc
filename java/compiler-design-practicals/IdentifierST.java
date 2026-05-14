import java.util.*;

public class IdentifierST {

    public static void main(String[] args) {

        Scanner sc = new Scanner(System.in);

        System.out.print("Enter identifier: ");
        String str = sc.next();

        int i;
        char ch = str.charAt(0);

        if (!(Character.isLetter(ch) || ch == '_')) {
            System.out.println("Invalid Identifier");
            return;
        }

        for (i = 1; i < str.length(); i++) {

            ch = str.charAt(i);

            if (!(Character.isLetterOrDigit(ch) || ch == '_')) {
                System.out.println("Invalid Identifier");
                return;
            }
        }

        System.out.println("Valid Identifier");
    }
}