import java.util.Scanner;

public class SugestedProb15 {
    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);
        if (!sc.hasNextInt())
            return;
        int N = sc.nextInt();
        int A = sc.nextInt();
        int B = sc.nextInt();
        int C = sc.nextInt();

        long prev = A * 0 * 0 + B * 0 * 0 + C * 0 * 0;
        int current = 1;
        int ans = 1;

        for (int x = 0; x < N; x++) {
            for (int y = 0; y < N; y++) {
                if (x == 0 && y == 0)
                    continue;
                long val = (long) A * x * x + (long) B * y * y + (long) C * x * y;
                if (val > prev)
                    current++;
                else
                    current = 1;
                if (current > ans)
                    ans = current;
                prev = val;
            }
        }
        System.out.println(ans);
    }
}
