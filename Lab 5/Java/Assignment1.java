import java.util.*;

public class Assignment1 {
    static void bfs(int start, List<List<Integer>> adj, int[] dist, int[] parent) {
        Arrays.fill(dist, -1);
        Queue<Integer> q = new LinkedList<>();
        dist[start] = 0;
        q.add(start);
        parent[start] = -1;
        while (!q.isEmpty()) {
            int u = q.poll();
            for (int v : adj.get(u)) {
                if (dist[v] == -1) {
                    dist[v] = dist[u] + 1;
                    parent[v] = u;
                    q.add(v);
                }
            }
        }
    }

    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);
        if (!sc.hasNextInt())
            return;
        int n = sc.nextInt();
        int m = sc.nextInt();
        int source = sc.nextInt();
        int dest = sc.nextInt();

        List<List<Integer>> adj = new ArrayList<>();
        for (int i = 0; i <= n; i++)
            adj.add(new ArrayList<>());

        for (int i = 0; i < m; i++) {
            int u = sc.nextInt();
            int v = sc.nextInt();
            adj.get(u).add(v);
            adj.get(v).add(u);
        }

        for (int i = 0; i <= n; i++)
            Collections.sort(adj.get(i));

        int[] distS = new int[n + 1];
        int[] parentS = new int[n + 1];
        bfs(source, adj, distS, parentS);

        if (distS[dest] == -1) {
            System.out.println("-1");
            return;
        }

        int[] distD = new int[n + 1];
        int[] parentD = new int[n + 1];
        bfs(dest, adj, distD, parentD);

        List<Integer> path = new ArrayList<>();
        path.add(source);
        int cur = source;
        int totalSteps = distS[dest];

        for (int i = 0; i < totalSteps; i++) {
            int bestNext = -1;
            for (int nxt : adj.get(cur)) {
                if (distS[nxt] == distS[cur] + 1) { // Forward check
                    if (distS[nxt] + distD[nxt] == totalSteps) { // Optimal path check
                        bestNext = nxt;
                        break; // Since sorted, first is lexicographically smallest
                    }
                }
            }
            if (bestNext != -1) {
                cur = bestNext;
                path.add(cur);
            }
        }

        System.out.println(totalSteps);
        for (int i = 0; i < path.size(); i++) {
            System.out.print(path.get(i) + (i == path.size() - 1 ? "" : " "));
        }
        System.out.println();
    }
}
