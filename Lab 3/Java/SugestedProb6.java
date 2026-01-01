import java.util.*;

public class SugestedProb6 {
    static List<Integer> res = new ArrayList<>();
    static int[] a;

    static void buildOrder(int l, int r) {
        if (l > r)
            return;
        int mid = (l + r) / 2;
        res.add(a[mid]);
        buildOrder(l, mid - 1);
        buildOrder(mid + 1, r);
    }

    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);
        if (!sc.hasNextInt())
            return;
        int n = sc.nextInt();
        a = new int[n];
        for (int i = 0; i < n; i++)
            a[i] = sc.nextInt();
        buildOrder(0, n - 1);
        for (int i = 0; i < res.size(); i++) {
            System.out.print(res.get(i) + (i == res.size() - 1 ? "" : " "));
        }
        System.out.println();
    }
}
