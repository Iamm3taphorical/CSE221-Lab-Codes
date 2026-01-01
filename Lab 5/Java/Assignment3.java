import java.util.*;

public class Assignment3 {
    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);
        if (!sc.hasNextInt())
            return;
        int n = sc.nextInt();
        int root = sc.nextInt();

        List<List<Integer>> adj = new ArrayList<>();
        for (int i = 0; i <= n; i++)
            adj.add(new ArrayList<>());

        for (int i = 0; i < n - 1; i++) {
            int u = sc.nextInt();
            int v = sc.nextInt();
            adj.get(u).add(v);
            adj.get(v).add(u);
        }

        int[] parent = new int[n + 1];
        // BFS to determine parent pointers (since it's a tree rooted at 'root')
        // Using BFS to topological sort (level order) to process bottom-up?
        // Python code uses reverse order of BFS visit to process subtrees.

        Queue<Integer> q = new LinkedList<>();
        List<Integer> order = new ArrayList<>();

        q.add(root);
        parent[root] = -1;

        while (!q.isEmpty()) {
            int u = q.poll();
            order.add(u);
            for (int v : adj.get(u)) {
                if (v != parent[u]) {
                    parent[v] = u;
                    q.add(v);
                }
            }
        }

        int[] subtree = new int[n + 1];
        Collections.reverse(order);

        for (int u : order) {
            int size = 1;
            for (int v : adj.get(u)) {
                if (v != parent[u]) {
                    size += subtree[v];
                }
            }
            subtree[u] = size;
        }

        int qCount = sc.nextInt();
        while (qCount-- > 0) {
            int queryNode = sc.nextInt();
            System.out.println(subtree[queryNode]);
        }
    }
}
