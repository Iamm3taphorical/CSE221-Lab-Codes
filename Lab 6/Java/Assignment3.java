import java.util.*;

public class Assignment3 {
    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);
        if (!sc.hasNextInt())
            return;
        int n = sc.nextInt();
        int m = sc.nextInt();
        int s = sc.nextInt();
        int q = sc.nextInt();

        List<List<Integer>> adj = new ArrayList<>();
        for (int i = 0; i <= n; i++)
            adj.add(new ArrayList<>());

        for (int i = 0; i < m; i++) {
            int u = sc.nextInt();
            int v = sc.nextInt();
            adj.get(u).add(v);
            adj.get(v).add(u);
        }

        int[] dist = new int[n + 1];
        Arrays.fill(dist, -1);
        Queue<Integer> queue = new LinkedList<>();

        for (int i = 0; i < s; i++) {
            int src = sc.nextInt();
            dist[src] = 0;
            queue.add(src);
        }

        int[] queries = new int[q];
        for (int i = 0; i < q; i++)
            queries[i] = sc.nextInt();

        while (!queue.isEmpty()) {
            int u = queue.poll();
            for (int v : adj.get(u)) {
                if (dist[v] == -1) {
                    dist[v] = dist[u] + 1;
                    queue.add(v);
                }
            }
        }

        for (int i = 0; i < q; i++) {
            System.out.print(dist[queries[i]] + (i == q - 1 ? "" : " "));
        }
        System.out.println();
    }
}
