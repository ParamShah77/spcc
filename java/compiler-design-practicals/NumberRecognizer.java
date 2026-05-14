import java.util.*;

public class NumberRecognizer {

    public static void main(String[] args) {

        Scanner sc = new Scanner(System.in);

        System.out.print("Enter number: ");
        String str = sc.next();

        if (str.matches("[0-9]+")) {
            System.out.println("Integer Number");
        }

        else if (str.matches("[0-9]+\\.[0-9]+")) {
            System.out.println("Floating Point Number");
        }

        else {
            System.out.println("Invalid Number");
        }
    }
}