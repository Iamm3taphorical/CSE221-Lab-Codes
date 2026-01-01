import java.util.Scanner;

public class Ass5up {
    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);
        if (!sc.hasNextInt())
            return;
        int t = sc.nextInt();
        while (t-- > 0) {
            int n = sc.nextInt();
            int m = sc.nextInt();

            int[] starts = new int[m];
            for (int i = 0; i < m; i++)
                starts[i] = sc.nextInt();

            int[] ends = new int[m];
            for (int i = 0; i < m; i++)
                ends[i] = sc.nextInt();

            int[] diff = new int[n];
            for (int i = 0; i < m; i++) {
                diff[starts[i] - 1]--;
                diff[ends[i] - 1]++;
            }

            for (int i = 0; i < n; i++) {
                System.out.print(diff[i] + (i == n - 1 ? "" : " "));
            }
            System.out.println();
        }
    }
}
