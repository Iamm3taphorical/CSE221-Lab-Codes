import java.util.Scanner;

public class ProblemE {
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

    static long fastSeries(long a, long n, long m) {
        if (n == 0)
            return 0;
        if (n == 1)
            return a % m;
        if (n % 2 == 0) {
            long half = fastSeries(a, n / 2, m);
            long pow = fastPower(a, n / 2, m);
            return (half + (pow * half) % m) % m;
        } else {
            return (fastSeries(a, n - 1, m) + fastPower(a, n, m)) % m;
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
            System.out.println(fastSeries(a, n, m));
        }
    }
}
