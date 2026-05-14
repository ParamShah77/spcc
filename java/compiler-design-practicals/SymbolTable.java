import java.util.*;

public class SymbolTable {

    public static void main(String[] args) {

        Scanner sc = new Scanner(System.in);

        System.out.print("Enter number of symbols: ");

        int n = sc.nextInt();

        sc.nextLine();

        int address = 0;

        System.out.println("\nSymbol Table");
        System.out.println("Symbol\tAddress");

        for (int i = 0; i < n; i++) {

            System.out.print("Enter symbol: ");

            String sym = sc.nextLine();

            System.out.printf("%s\t%04d\n",
                    sym, address);

            address += 3;
        }
    }
}