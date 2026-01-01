import java.util.*;

public class Ass6up {
    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);
        if (!sc.hasNextInt())
            return;
        int t = sc.nextInt();
        while (t-- > 0) {
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
}
