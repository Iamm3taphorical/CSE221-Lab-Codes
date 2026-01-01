import java.util.Scanner;

public class SugestedProb5 {
    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);
        if (!sc.hasNextLong())
            return;
        long a = sc.nextLong();
        long n = sc.nextLong();
        long mod = 107;
        long res = 1;
        a %= mod;
        while (n > 0) {
            if (n % 2 == 1)
                res = (res * a) % mod;
            a = (a * a) % mod;
            n /= 2;
        }
        System.out.println(res);
    }
}
