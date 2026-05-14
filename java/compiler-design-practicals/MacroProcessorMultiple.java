import java.util.*;

public class MacroProcessorMultiple {

    public static void main(String[] args) {

        Scanner sc = new Scanner(System.in);

        ArrayList<String> deftab =
                new ArrayList<>();

        ArrayList<String> namtab =
                new ArrayList<>();

        System.out.print("Enter number of lines: ");

        int n = sc.nextInt();

        sc.nextLine();

        int start = 0;

        System.out.println("Enter macro definitions:");

        for (int i = 0; i < n; i++) {

            String line = sc.nextLine();

            deftab.add(line);

            // Detect MACRO line
            if (line.contains("MACRO")) {

                String parts[] = line.split(" ");

                String macroName = parts[0];

                start = i + 1;

                namtab.add(
                        macroName
                                + "\tStart:"
                                + start);
            }

            // Detect MEND
            if (line.equals("MEND")) {

                int end = i + 1;

                int last =
                        namtab.size() - 1;

                namtab.set(last,
                        namtab.get(last)
                                + "\tEnd:"
                                + end);
            }
        }

        // Print DEFTAB
        System.out.println("\nDEFTAB");

        for (int i = 0; i < deftab.size(); i++) {

            System.out.println(
                    (i + 1)
                            + "\t"
                            + deftab.get(i));
        }

        // Print NAMTAB
        System.out.println("\nNAMTAB");

        System.out.println(
                "MacroName\tStart\tEnd");

        for (String s : namtab) {

            System.out.println(s);
        }
    }
}