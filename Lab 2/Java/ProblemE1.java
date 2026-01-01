import java.util.Scanner;

public class ProblemE1 {
    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);
        if (!sc.hasNextInt())
            return;
        int n = sc.nextInt();
        int k = sc.nextInt();
        int[] a = new int[n];
        for (int i = 0; i < n; i++)
            a[i] = sc.nextInt();

        int l = 0, r = 0;
        long sum = 0;
        int maxLen = 0;

        while (r < n) {
            sum += a[r];
            while (sum > k && l <= r) {
                sum -= a[l];
                l++;
            }
            if (sum <= k) {
                int len = r - l + 1;
                if (len > maxLen)
                    maxLen = len;
            }
            r++;
        }
        System.out.println(maxLen);
    }
}
