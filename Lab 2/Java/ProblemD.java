import java.util.Scanner;

public class ProblemD {
    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);
        if (!sc.hasNextInt())
            return;
        int n = sc.nextInt();
        int[] a = new int[n];
        for (int i = 0; i < n; i++)
            a[i] = sc.nextInt();
        int m = sc.nextInt();
        int[] b = new int[m];
        for (int i = 0; i < m; i++)
            b[i] = sc.nextInt();

        int l = 0, r = 0;
        StringBuilder sb = new StringBuilder();
        while (l < n && r < m) {
            if (a[l] <= b[r]) {
                sb.append(a[l]).append(" ");
                l++;
            } else {
                sb.append(b[r]).append(" ");
                r++;
            }
        }
        while (l < n) {
            sb.append(a[l]).append(" ");
            l++;
        }
        while (r < m) {
            sb.append(b[r]).append(" ");
            r++;
        }
        System.out.println(sb.toString().trim());
    }
}
