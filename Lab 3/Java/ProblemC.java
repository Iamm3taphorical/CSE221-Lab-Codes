import java.util.Scanner;

public class ProblemC {
    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);
        if (!sc.hasNextLong())
            return;
        long a = sc.nextLong();
        long b = sc.nextLong();
        long mod = 107;
        long result = 1;
        a %= mod;
        while (b > 0) {
            if (b % 2 == 1)
                result = (result * a) % mod;
            a = (a * a) % mod;
            b /= 2;
        }
        System.out.println(result);
    }
}
