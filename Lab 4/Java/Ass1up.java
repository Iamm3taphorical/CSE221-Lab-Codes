import java.util.Scanner;

public class Ass1up {
    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);
        if (!sc.hasNextInt())
            return;
        int t = sc.nextInt();
        while (t-- > 0) {
            int n = sc.nextInt();
            int m = sc.nextInt();
            int[] diff = new int[n];

            // Reading start nodes
            // Wait, input format: "start_var = list(map(int, input().split()))"
            // Start nodes are all on one line?
            // "end_var = list(map(int, input().split()))"
            // Both are lists of size m.

            // Java scanner reads token by token.
            // I need to read m integers for starts, then m integers for ends.
            // Problem: Input might be split across lines or all in one line. Scanner
            // handles whitespace.
            // But I need to store starts to process later or process in parallel?
            // Python reads starts list, then ends list.

            int[] starts = new int[m];
            for (int i = 0; i < m; i++)
                starts[i] = sc.nextInt();

            int[] ends = new int[m];
            for (int i = 0; i < m; i++)
                ends[i] = sc.nextInt();

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
