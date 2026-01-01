import java.util.Scanner;

public class SugestedProb10 {
    static long mod = 1000000007;

    static long[][] multiply(long[][] A, long[][] B) {
        long[][] C = new long[2][2];
        for (int i = 0; i < 2; i++) {
            for (int j = 0; j < 2; j++) {
                for (int k = 0; k < 2; k++) {
                    C[i][j] = (C[i][j] + A[i][k] * B[k][j]) % mod;
                }
            }
        }
        return C;
    }

    static long[][] power(long[][] A, long x) {
        long[][] res = { { 1, 0 }, { 0, 1 } };
        while (x > 0) {
            if (x % 2 == 1)
                res = multiply(res, A);
            A = multiply(A, A);
            x /= 2;
        }
        return res;
    }

    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);
        if (!sc.hasNextInt())
            return;
        int t = sc.nextInt();
        while (t-- > 0) {
            long a11 = sc.nextLong();
            long a12 = sc.nextLong();
            long a21 = sc.nextLong();
            long a22 = sc.nextLong();
            long x = sc.nextLong();
            long[][] mat = { { a11, a12 }, { a21, a22 } };
            long[][] res = power(mat, x);
            System.out.println(res[0][0] + " " + res[0][1]);
            System.out.println(res[1][0] + " " + res[1][1]);
        }
    }
}
