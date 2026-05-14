import java.util.*;

public class MacroExpansion {

    public static void main(String[] args) {

        Scanner sc = new Scanner(System.in);

        // Store macro body
        ArrayList<String> macroBody =
                new ArrayList<>();

        System.out.print("Enter macro name: ");

        String macroName = sc.nextLine();

        System.out.print("Enter number of macro lines: ");

        int n = sc.nextInt();

        sc.nextLine();

        System.out.println(
                "Enter macro body:");

        // Input macro body
        for (int i = 0; i < n; i++) {

            macroBody.add(sc.nextLine());
        }

        System.out.print(
                "Enter number of program lines: ");

        int m = sc.nextInt();

        sc.nextLine();

        ArrayList<String> program =
                new ArrayList<>();

        System.out.println(
                "Enter program:");

        // Input program
        for (int i = 0; i < m; i++) {

            program.add(sc.nextLine());
        }

        // Expansion
        System.out.println(
                "\nExpanded Program:");

        for (String line : program) {

            // If macro call found
            if (line.equals(macroName)) {

                for (String body : macroBody) {

                    System.out.println(body);
                }
            }

            else {

                System.out.println(line);
            }
        }
    }
}