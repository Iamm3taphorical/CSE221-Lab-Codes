import java.util.*;

public class Assignment3Fix {
    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);
        if (!sc.hasNextLine())
            return;
        // Read n (first line)
        if (!sc.hasNextInt())
            return;
        int n = sc.nextInt();
        sc.nextLine(); // consume newline

        int[][] matrix = new int[n][n];

        for (int i = 0; i < n; i++) {
            String line = sc.nextLine();
            if (line.trim().isEmpty())
                continue;
            String[] parts = line.trim().split("\\s+");
            // parts[0] is count?
            // Iterate from index 1.
            for (int j = 1; j < parts.length; j++) {
                int col = Integer.parseInt(parts[j]);
                if (col >= 0 && col < n) {
                    matrix[i][col] = 1;
                }
            }
        }

        for (int i = 0; i < n; i++) {
            for (int j = 0; j < n; j++) {
                System.out.print(matrix[i][j] + (j == n - 1 ? "" : " "));
            }
            System.out.println();
        }
    }
}
