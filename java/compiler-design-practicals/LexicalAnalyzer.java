import java.util.*;

public class LexicalAnalyzer {

    public static void main(String[] args) {

        Scanner sc = new Scanner(System.in);

        String keywords[] = {
                "int", "float", "if",
                "else", "while", "switch"
        };

        System.out.print("Enter token: ");
        String str = sc.next();

        boolean isKeyword = false;

        for (String k : keywords) {
            if (str.equals(k)) {
                isKeyword = true;
                break;
            }
        }

        if (isKeyword) {
            System.out.println(str + " is a Keyword");
        }

        else if (str.matches("[a-zA-Z_][a-zA-Z0-9_]*")) {
            System.out.println(str + " is an Identifier");
        }

        else {
            System.out.println("Invalid Token");
        }
    }
}