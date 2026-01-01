import java.util.Scanner;

public class ProblemH {
    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);
        if (!sc.hasNextInt())
            return;
        int t = sc.nextInt();
        while (t-- > 0) {
            long k = sc.nextLong();
            long x = sc.nextLong();
            long l = 1;
            long r = k * x;
            while (l < r) {
                long m = (l + r) / 2;
                long c = m - (m / x);
                if (c < k)
                    l = m + 1;
                else
                    r = m;
            }
            System.out.println(l);
        }
    }
}
