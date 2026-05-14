import java.util.*;

public class BasicBlocks {

    public static void main(String[] args) {

        Scanner sc = new Scanner(System.in);

        System.out.print("Enter number of statements: ");
        int n = sc.nextInt();

        sc.nextLine();

        String stmt[] = new String[n];

        for (int i = 0; i < n; i++) {

            System.out.print("Statement " + (i+1) + ": ");
            stmt[i] = sc.nextLine();
        }

        Set<Integer> leaders = new TreeSet<>();

        leaders.add(0);

        for (int i = 0; i < n; i++) {

            if (stmt[i].contains("goto")) {

                String parts[] = stmt[i].split(" ");

                int target =
                        Integer.parseInt(parts[parts.length - 1]);

                leaders.add(target - 1);

                if (i + 1 < n) {
                    leaders.add(i + 1);
                }
            }
        }

        List<Integer> list =
                new ArrayList<>(leaders);

        System.out.println("\nBasic Blocks:");

        for (int i = 0; i < list.size(); i++) {

            int start = list.get(i);

            int end;

            if (i == list.size() - 1) {
                end = n - 1;
            }

            else {
                end = list.get(i + 1) - 1;
            }

            System.out.println("\nBlock "
                    + (i + 1));

            for (int j = start; j <= end; j++) {

                System.out.println(
                        (j + 1) + ". "
                                + stmt[j]);
            }
        }
    }
}