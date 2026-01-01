import java.util.*;

public class Ass3up {
    static int gcd(int a, int b) {
        while (b != 0) {
            int temp = b;
            b = a % b;
            a = temp;
        }
        return a;
    }

    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);
        if (!sc.hasNextInt())
            return;
        int t = sc.nextInt();
        while (t-- > 0) {
            int n = sc.nextInt();
            int q = sc.nextInt();

            List<List<Integer>> adj = new ArrayList<>();
            for (int i = 0; i <= n; i++)
                adj.add(new ArrayList<>());

            for (int i = 1; i <= n; i++) {
                for (int j = 1; j <= n; j++) {
                    if (i != j && gcd(i, j) == 1) {
                        adj.get(i).add(j);
                    }
                }
            }

            while (q-- > 0) {
                int u = sc.nextInt();
                int k = sc.nextInt();
                if (k > adj.get(u).size()) {
                    System.out.println("-1");
                } else {
                    System.out.println(adj.get(u).get(k - 1));
                }
            }
        }
    }
}
