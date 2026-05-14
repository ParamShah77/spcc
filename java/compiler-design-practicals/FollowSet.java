import java.util.*;

public class FollowSet {

    public static void main(String[] args) {

        Scanner sc = new Scanner(System.in);

        System.out.print("Enter production (Example S=AB): ");
        String prod = sc.next();

        char lhs = prod.charAt(0);

        String rhs = prod.substring(2);

        Map<Character, Set<Character>> follow = new HashMap<>();

        for (char c : rhs.toCharArray()) {

            if (Character.isUpperCase(c)) {
                follow.put(c, new HashSet<>());
            }
        }

        for (int i = 0; i < rhs.length() - 1; i++) {

            char current = rhs.charAt(i);
            char next = rhs.charAt(i + 1);

            if (Character.isUpperCase(current)) {
                follow.get(current).add(next);
            }
        }

        follow.put(lhs, new HashSet<>());
        follow.get(lhs).add('$');

        for (char c : follow.keySet()) {
            System.out.println("FOLLOW(" + c + ") = " + follow.get(c));
        }
    }
}