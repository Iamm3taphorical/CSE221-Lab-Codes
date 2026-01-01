import java.util.Scanner;

public class Assignment5 {
    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);
        if (!sc.hasNextInt())
            return;
        // Logic same as Ass1up / Degree Difference
        // Assumes single test case or input format matches Assignment5.py output?
        // Assignment5.py output shows loop for t_var? No.
        // Step 352 output for Assignment5.py starts with:
        // "vertices_var, edges_var = map(int, input().split())"
        // NO t_var loop!
        // This is DIFFERENT from Ass1up.py which had "while t_var > 0".
        // Assignment5.py processes ONE test case.

        // I must be careful.
        // Ass1up.py had t iterations.
        // Assignment5.py has NO t loop (based on Step 352 output block 1).

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
