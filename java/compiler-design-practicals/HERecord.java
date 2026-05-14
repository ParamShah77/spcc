import java.util.*;

public class HERecord {

    public static void main(String[] args) {

        Scanner sc = new Scanner(System.in);

        System.out.print("Enter program name: ");
        String name = sc.next();

        System.out.print("Enter start address: ");
        String start = sc.next();

        System.out.print("Enter program length: ");
        String length = sc.next();

        System.out.println("\nHeader Record:");
        System.out.println("H^" + name
                + "^" + start
                + "^" + length);

        System.out.println("\nEnd Record:");
        System.out.println("E^" + start);
    }
}