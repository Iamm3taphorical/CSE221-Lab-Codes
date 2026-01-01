import java.util.*;

public class Ass7up {
    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);
        if (!sc.hasNextInt())
            return;
        int t = sc.nextInt();
        while (t-- > 0) {
            int r = sc.nextInt();
            int c = sc.nextInt();
            int k = sc.nextInt();

            Set<String> positions = new HashSet<>();
            int[][] knightPos = new int[k][2];

            for (int i = 0; i < k; i++) {
                int rr = sc.nextInt();
                int cc = sc.nextInt();
                knightPos[i][0] = rr;
                knightPos[i][1] = cc;
                positions.add(rr + "," + cc);
            }

            boolean attack = false;
            for (int i = 0; i < k; i++) {
                int cr = knightPos[i][0];
                int cc = knightPos[i][1];

                int[][] moves = {
                        { cr - 2, cc - 1 }, { cr - 2, cc + 1 },
                        { cr - 1, cc - 2 }, { cr - 1, cc + 2 },
                        { cr + 1, cc - 2 }, { cr + 1, cc + 2 },
                        { cr + 2, cc - 1 }, { cr + 2, cc + 1 }
                };

                for (int[] move : moves) {
                    if (positions.contains(move[0] + "," + move[1])) {
                        attack = true;
                        break;
                    }
                }
                if (attack)
                    break;
            }

            if (attack)
                System.out.println("YES");
            else
                System.out.println("NO");
        }
    }
}
