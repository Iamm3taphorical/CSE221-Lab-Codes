import java.util.Scanner;

public class SugestedProb1 {
    static long fastPower(long a, long b, long mod) {
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

    static long fastSeries(long a, long n, long mod) {
        if (n == 0)
            return 0;
        if (n == 1)
            return a % mod;
        if (n % 2 == 0) {
            long half = fastSeries(a, n / 2, mod);
            long pow = fastPower(a, n / 2, mod);
            return (half * (1 + pow)) % mod;
        } else {
            return (fastSeries(a, n - 1, mod) + fastPower(a, n, mod)) % mod;
        }
    }

    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);
        if (!sc.hasNextLong())
            return;
        long a = sc.nextLong();
        long n = sc.nextLong();
        long mod = 107;
        System.out.println(fastSeries(a, n, mod));
    }
}
