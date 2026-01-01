import java.util.Scanner;

public class ProblemB2 {
    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);
        if (!sc.hasNextInt())
            return;
        int n = sc.nextInt();
        int m = sc.nextInt();
        int k = sc.nextInt();
        int[] a = new int[n];
        for (int i = 0; i < n; i++)
            a[i] = sc.nextInt();
        int[] b = new int[m];
        for (int i = 0; i < m; i++)
            b[i] = sc.nextInt();

        int l = 0;
        int r = m - 1;
        int bL = 0;
        int bR = 0;
        int bD = Integer.MAX_VALUE;

        while (l < n && r >= 0) {
            int sum = a[l] + b[r];
            int diff = Math.abs(sum - k);
            if (diff < bD) {
                bD = diff;
                bL = l;
                bR = r;
            }
            if (sum < k) {
                l++;
            } else {
                r--;
            }
        }
        System.out.println((bL + 1) + " " + (bR + 1));
    }
}
