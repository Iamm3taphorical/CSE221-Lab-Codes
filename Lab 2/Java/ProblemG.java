import java.util.*;

public class ProblemG {
    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);
        if (!sc.hasNextInt())
            return;
        int n = sc.nextInt();
        int q = sc.nextInt();
        int[] a = new int[n];
        for (int i = 0; i < n; i++)
            a[i] = sc.nextInt();

        StringBuilder sb = new StringBuilder();
        for (int k = 0; k < q; k++) {
            int x = sc.nextInt();
            int y = sc.nextInt();

            int l = 0, r = n;
            while (l < r) {
                int mid = (l + r) / 2;
                if (a[mid] < x)
                    l = mid + 1;
                else
                    r = mid;
            }
            int lb = l;

            l = 0;
            r = n;
            while (l < r) {
                int mid = (l + r) / 2;
                if (a[mid] <= y)
                    l = mid + 1;
                else
                    r = mid;
            }
            int ub = l;
            sb.append(ub - lb).append("\n");
        }
        System.out.print(sb.toString());
    }
}
