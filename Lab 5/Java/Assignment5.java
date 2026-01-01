import java.util.*;

public class Assignment5 {
    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);
        if (!sc.hasNextInt())
            return;
        int rows = sc.nextInt();
        int cols = sc.nextInt();
        char[][] grid = new char[rows][cols];

        for (int i = 0; i < rows; i++) {
            String line = sc.next();
            grid[i] = line.toCharArray();
        }

        boolean[][] visited = new boolean[rows][cols];
        int maxDiamonds = 0;
        int[][] dirs = { { 1, 0 }, { 0, 1 }, { -1, 0 }, { 0, -1 } };

        for (int i = 0; i < rows; i++) {
            for (int j = 0; j < cols; j++) {
                if (grid[i][j] != '#' && !visited[i][j]) {
                    int diamonds = 0;
                    Queue<int[]> q = new LinkedList<>();
                    q.add(new int[] { i, j });
                    visited[i][j] = true;

                    while (!q.isEmpty()) {
                        int[] curr = q.poll();
                        if (grid[curr[0]][curr[1]] == 'D')
                            diamonds++;

                        for (int[] d : dirs) {
                            int ni = curr[0] + d[0];
                            int nj = curr[1] + d[1];
                            if (ni >= 0 && ni < rows && nj >= 0 && nj < cols
                                    && !visited[ni][nj] && grid[ni][nj] != '#') {
                                visited[ni][nj] = true;
                                q.add(new int[] { ni, nj });
                            }
                        }
                    }
                    if (diamonds > maxDiamonds)
                        maxDiamonds = diamonds;
                }
            }
        }
        System.out.println(maxDiamonds);
    }
}
