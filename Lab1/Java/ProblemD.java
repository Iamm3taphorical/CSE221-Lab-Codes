import java.util.Scanner;

public class ProblemD {
    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);
        if (sc.hasNextInt()) {
            int t = sc.nextInt();
            for (int i = 0; i < t; i++) {
                int n = sc.nextInt();
                int[] arr = new int[n];
                for (int j = 0; j < n; j++) {
                    arr[j] = sc.nextInt();
                }
                boolean flag = true;
                for (int k = 1; k < n; k++) {
                    if (arr[k - 1] > arr[k]) {
                        flag = false;
                        break;
                    }
                }
                if (flag) {
                    System.out.println("YES");
                } else {
                    System.out.println("NO");
                }
            }
        }
    }
}
