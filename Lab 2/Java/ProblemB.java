import java.util.Scanner;

public class ProblemB {
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

        int left = 0;
        int right = m - 1;
        int bestI = 0;
        int bestJ = 0;
        int bestDiff = Integer.MAX_VALUE;

        while (left < n && right >= 0) {
            int sum = a[left] + b[right];
            int diff = Math.abs(sum - k);
            if (diff < bestDiff) {
                bestDiff = diff;
                bestI = left;
                bestJ = right;
            }
            if (sum > k) {
                right--;
            } else {
                left++;
            }
        }
        System.out.println((bestI + 1) + " " + (bestJ + 1));
    }
}
