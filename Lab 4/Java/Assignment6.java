import java.util.*;

public class Assignment6 {
    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);
        if (!sc.hasNextInt())
            return;
        // Assignment6.py output Step 352 Block 2:
        // "size_var = int(input())"
        // NO t_var loop.

        int n = sc.nextInt();
        int r = sc.nextInt();
        int c = sc.nextInt();

        int[][] moves = {
                { r - 1, c - 1 }, { r - 1, c }, { r - 1, c + 1 },
                { r, c - 1 }, { r, c + 1 },
                { r + 1, c - 1 }, { r + 1, c }, { r + 1, c + 1 }
        };

        List<int[]> validMoves = new ArrayList<>();
        for (int[] move : moves) {
            int nr = move[0];
            int nc = move[1];
            if (nr > 0 && nr <= n && nc > 0 && nc <= n) {
                validMoves.add(move);
            }
        }

        System.out.println(validMoves.size());
        for (int[] move : validMoves) {
            System.out.println(move[0] + " " + move[1]);
        }
    }
}
