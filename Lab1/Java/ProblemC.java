import java.util.Scanner;

public class ProblemC {
    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);
        if (sc.hasNextInt()) {
            int t = sc.nextInt();
            for (int i = 0; i < t; i++) {
                long n = sc.nextLong();
                long res = (n * (n + 1)) / 2;
                System.out.println(res);
            }
        }
    }
}
