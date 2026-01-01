import java.util.Scanner;

public class SugestedProb9 {
    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);
        if (!sc.hasNextInt())
            return;
        int n = sc.nextInt();
        long[] a = new long[n];
        for (int i = 0; i < n; i++)
            a[i] = sc.nextLong();

        long maxSum = Long.MIN_VALUE;
        long currentSum = 0;
        int start = 0;
        int tempStart = 0;
        int end = 0;

        for (int i = 0; i < n; i++) {
            currentSum += a[i];
            if (currentSum > maxSum) {
                maxSum = currentSum;
                start = tempStart;
                end = i;
            }
            if (currentSum < 0) {
                currentSum = 0;
                tempStart = i + 1;
            }
        }
        System.out.print((start + 1) + " " + (end + 1));
    }
}
