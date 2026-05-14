import java.util.*;

public class BlockTable {

    public static void main(String[] args) {

        Scanner sc = new Scanner(System.in);

        System.out.print("Enter number of blocks: ");

        int n = sc.nextInt();

        sc.nextLine();

        int address = 0;

        System.out.println("\nBLOCK TABLE");

        System.out.println("BlockNo\tName\tAddress");

        for (int i = 0; i < n; i++) {

            System.out.print("Enter block name: ");

            String name = sc.nextLine();

            System.out.printf("%d\t%s\t%04d\n",
                    i, name, address);

            address += 100;
        }
    }
}