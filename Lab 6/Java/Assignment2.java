import java.util.*;

public class Assignment2 {
    static class Result {
        int node;
        int dist;

        public Result(int node, int dist) {
            this.node = node;
            this.dist = dist;
        }
    }

    static Result bfs(int start, List<List<Integer>> adj, int n) {
        int[] dist = new int[n + 1];
        Arrays.fill(dist, -1);
        Queue<Integer> q = new LinkedList<>();

        dist[start] = 0;
        q.add(start);

        int farthestNode = start;
        int maxDist = 0;

        while (!q.isEmpty()) {
            int u = q.poll();
            if (dist[u] > maxDist) {
                maxDist = dist[u];
                farthestNode = u;
            }

            for (int v : adj.get(u)) {
                if (dist[v] == -1) {
                    dist[v] = dist[u] + 1;
                    q.add(v);
                }
            }
        }
        return new Result(farthestNode, maxDist);
    }

    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);
        if (!sc.hasNextInt())
            return;
        int n = sc.nextInt();
        // Python code Output Block 2:
        // "input().split()" -> likely reading u, v lines for edges.
        // It's a tree (n-1 edges typically).
        // Python line: "for i in range(n-1)?" Or just m edges?
        // Lab 6 usually assumes Tree for Diameter.
        // I'll assume n-1 edges.

        List<List<Integer>> adj = new ArrayList<>();
        for (int i = 0; i <= n; i++)
            adj.add(new ArrayList<>());

        for (int i = 0; i < n - 1; i++) {
            int u = sc.nextInt();
            int v = sc.nextInt();
            adj.get(u).add(v);
            adj.get(v).add(u);
        }

        Result r1 = bfs(1, adj, n);
        Result r2 = bfs(r1.node, adj, n);

        System.out.println(r2.dist);
        System.out.println(r1.node + " " + r2.node);
    }
}
