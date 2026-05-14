import java.util.*;

public class DRRecord {

    public static void main(String[] args) {

        Scanner sc = new Scanner(System.in);

        System.out.print("Enter number of EXTDEF symbols: ");

        int d = sc.nextInt();

        sc.nextLine();

        String def[] = new String[d];

        int addr = 3;

        String dRecord = "D^";

        System.out.println("Enter EXTDEF symbols:");

        for (int i = 0; i < d; i++) {

            def[i] = sc.nextLine();

            dRecord += def[i]
                    + "^"
                    + String.format("%06d", addr)
                    + "^";

            addr += 6;
        }

        System.out.print("\nEnter number of EXTREF symbols: ");

        int r = sc.nextInt();

        sc.nextLine();

        String rRecord = "R^";

        System.out.println("Enter EXTREF symbols:");

        for (int i = 0; i < r; i++) {

            String sym = sc.nextLine();

            rRecord += sym + "^";
        }

        System.out.println("\nD Record:");
        System.out.println(dRecord);

        System.out.println("\nR Record:");
        System.out.println(rRecord);

        System.out.println("\nLocal Symbol Table");

        addr = 3;

        System.out.println("Symbol\tValue");

        for (int i = 0; i < d; i++) {

            System.out.printf("%s\t%06d\n",
                    def[i], addr);

            addr += 6;
        }
    }
}