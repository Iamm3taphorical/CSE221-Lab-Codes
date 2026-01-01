import java.util.Scanner;

public class ProblemB {
    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);
        if (sc.hasNextInt()) {
            int t = sc.nextInt();
            for (int i = 0; i < t; i++) {
                String skip = sc.next();
                double a = sc.nextDouble();
                String op = sc.next();
                double b = sc.nextDouble();
                double res = 0;
                if (op.equals("+")) res = a + b;
                else if (op.equals("-")) res = a - b;
                else if (op.equals("*")) res = a * b;
                else if (op.equals("/")) res = a / b;
                System.out.printf("%.6f%n", res);
            }
        }
    }
}
