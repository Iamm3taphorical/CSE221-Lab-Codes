import java.util.*;

public class ProblemG {
    static class Pair {
        int id, mark;

        public Pair(int i, int m) {
            id = i;
            mark = m;
        }
    }

    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);
        if (!sc.hasNextInt())
            return;
        int t = sc.nextInt();
        for (int tc = 0; tc < t; tc++) {
            int n = sc.nextInt();
            int[] ids = new int[n];
            for (int i = 0; i < n; i++)
                ids[i] = sc.nextInt();
            int[] marks = new int[n];
            for (int i = 0; i < n; i++)
                marks[i] = sc.nextInt();
            Pair[] pairs = new Pair[n];
            for (int i = 0; i < n; i++)
                pairs[i] = new Pair(ids[i], marks[i]);

            Pair[] target = new Pair[n];
            for (int i = 0; i < n; i++)
                target[i] = pairs[i];

            for (int i = 0; i < n; i++) {
                for (int j = 0; j < n - 1; j++) {
                    boolean swap = false;
                    if (target[j + 1].mark > target[j].mark)
                        swap = true;
                    else if (target[j + 1].mark == target[j].mark && target[j + 1].id < target[j].id)
                        swap = true;
                    if (swap) {
                        Pair tmp = target[j];
                        target[j] = target[j + 1];
                        target[j + 1] = tmp;
                    }
                }
            }

            Map<Integer, Integer> idToTargetIdx = new HashMap<>();
            for (int i = 0; i < n; i++)
                idToTargetIdx.put(target[i].id, i);

            int[] perm = new int[n];
            for (int i = 0; i < n; i++)
                perm[i] = idToTargetIdx.get(pairs[i].id);

            boolean[] visited = new boolean[n];
            int minSwaps = 0;
            for (int i = 0; i < n; i++) {
                if (!visited[i]) {
                    int cycleLen = 0;
                    int cur = i;
                    while (!visited[cur]) {
                        visited[cur] = true;
                        cycleLen++;
                        cur = perm[cur];
                    }
                    if (cycleLen > 0)
                        minSwaps += (cycleLen - 1);
                }
            }
            System.out.println("Minimum swaps: " + minSwaps);
            for (int i = 0; i < n; i++)
                System.out.println("ID: " + target[i].id + " Mark: " + target[i].mark);
        }
    }
}
