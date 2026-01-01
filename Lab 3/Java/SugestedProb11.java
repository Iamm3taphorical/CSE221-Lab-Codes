import java.util.Scanner;

public class SugestedProb11 {
    static long power(long a, long b, long mod) {
        long res = 1;
        a %= mod;
        while (b > 0) {
            if (b % 2 == 1)
                res = (res * a) % mod;
            a = (a * a) % mod;
            b /= 2;
        }
        return res;
    }

    static long series(long a, long n, long mod) {
        if (n == 0)
            return 0;
        if (n == 1)
            return a % mod;
        if (n % 2 == 0) {
            long half = series(a, n / 2, mod);
            long p = power(a, n / 2, mod);
            return (half + (p * half) % mod) % mod;
        } else {
            return (series(a, n - 1, mod) + power(a, n, mod)) % mod;
        }
    }

    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);
        if (!sc.hasNextInt())
            return;
        int t = sc.nextInt();
        while (t-- > 0) {
            long a = sc.nextLong();
            long n = sc.nextLong();
            long m = sc.nextLong();
            System.out.println(series(a, n, m));
        }
    }
}
