import java.util.Scanner;

public class ProblemA {
    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);
        if (sc.hasNextInt()) {
            int t = sc.nextInt();
            for (int i = 0; i < t; i++) {
                int n = sc.nextInt();
                if (n % 2 == 0) {
                    System.out.println(n + " is an Even number.");
                } else {
                    System.out.println(n + " is an Odd number.");
                }
            }
        }
    }
}
