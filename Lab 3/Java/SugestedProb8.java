import java.util.Scanner;

public class SugestedProb8 {
    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);
        if (!sc.hasNextInt())
            return;
        int n = sc.nextInt();
        long[] a = new long[n];
        for (int i = 0; i < n; i++)
            a[i] = sc.nextLong();

        // Using int for sum as in Python example? "max_sum_var = -float('inf')".
        // Values can be large? I'll use long to be safe, but cast to int for print if
        // needed.
        // Python code: `sys.stdout.write(str(int(max_sum_var)))`

        long maxSum = Long.MIN_VALUE;
        long currentSum = 0;

        for (int i = 0; i < n; i++) {
            currentSum += a[i];
            if (currentSum > maxSum)
                maxSum = currentSum;
            if (currentSum < 0)
                currentSum = 0;
        }
        System.out.print(maxSum);
    }
}
