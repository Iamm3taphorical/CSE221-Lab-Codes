import java.util.*;

public class Assignment6 {
    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);
        if (!sc.hasNextInt())
            return;
        int n = sc.nextInt();
        int m = sc.nextInt();

        List<List<Integer>> adj = new ArrayList<>();
        for (int i = 0; i <= n; i++)
            adj.add(new ArrayList<>());

        for (int i = 0; i < m; i++) {
            int u = sc.nextInt();
            int v = sc.nextInt();
            adj.get(u).add(v);
        }

        int[] visited = new int[n + 1];
        int[] recStack = new int[n + 1];
        boolean hasCycle = false;

        for (int i = 1; i <= n; i++) {
            if (visited[i] == 0) {
                if (dfsCheck(i, adj, visited, recStack)) {
                    hasCycle = true;
                    break;
                }
            }
        }

        if (hasCycle)
            System.out.println("YES");
        else
            System.out.println("NO");
    }

    static boolean dfsCheck(int u, List<List<Integer>> adj, int[] visited, int[] recStack) {
        visited[u] = 1;
        recStack[u] = 1;

        for (int v : adj.get(u)) {
            if (visited[v] == 0) {
                if (dfsCheck(v, adj, visited, recStack))
                    return true;
            } else if (recStack[v] == 1) {
                return true;
            }
        }

        recStack[u] = 0;
        return false;
    }
}
