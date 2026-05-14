import java.util.*;

public class OperatorRecognizer {

    public static void main(String[] args) {

        Scanner sc = new Scanner(System.in);

        System.out.print("Enter operator: ");
        String op = sc.next();

        switch(op) {

            case "+":
            case "-":
            case "*":
            case "/":
                System.out.println("Arithmetic Operator");
                break;

            case "<":
            case ">":
            case "==":
                System.out.println("Relational Operator");
                break;

            case "=":
                System.out.println("Assignment Operator");
                break;

            default:
                System.out.println("Invalid Operator");
        }
    }
}