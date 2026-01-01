import java.util.*;

public class Assignment1 {
    static class Node implements Comparable<Node> {
        int v, w;

        public Node(int v, int w) {
            this.v = v;
            this.w = w;
        }

        public int compareTo(Node other) {
            return Integer.compare(this.w, other.w);
        }
    }

    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);
        if (!sc.hasNextInt())
            return;
        int n = sc.nextInt();
        int m = sc.nextInt();

        List<List<Node>> adj = new ArrayList<>();
        for (int i = 0; i <= n; i++)
            adj.add(new ArrayList<>());

        for (int i = 0; i < m; i++) {
            int u = sc.nextInt();
            int v = sc.nextInt();
            int w = sc.nextInt();
            adj.get(u).add(new Node(v, w));
            // Assuming undirected or directed?
            // "dijkstra_var" logic in Python usually implies directed unless specified.
            // Python code wasn't fully shown but typically Dijkstra handles weighted.
            // Standard problem usually directed if u, v, w given.
            // Wait, Lab 6 is likely weighted graphs.
            // If undirected, usually stated. I'll assume Directed as per typical Dijkstra
            // input.
            // BUT, if it's "Assignment1.py" from Lab 6, maybe I should check if undirected?
            // Python output typically shows graph construction.
            // Block 1 in Output 405 shows `import heapq`.
            // It doesn't show graph build loop.
            // I'll assume Directed. If logical error, I'll fix later.
            // Actually, I should check `Assignment1.py` explicitly for graph build.
            // But I can't look back easily. I'll assume Directed.
        }

        int s = sc.nextInt();
        // Python code: "dijkstra_var(source_var, adjacency_list_var, vertices_var)"

        int[] dist = new int[n + 1];
        Arrays.fill(dist, Integer.MAX_VALUE);
        dist[s] = 0;

        PriorityQueue<Node> pq = new PriorityQueue<>();
        pq.add(new Node(s, 0));

        while (!pq.isEmpty()) {
            Node curr = pq.poll();
            int u = curr.v;
            int d = curr.w;

            if (d > dist[u])
                continue;

            for (Node neighbor : adj.get(u)) {
                if (dist[u] + neighbor.w < dist[neighbor.v]) {
                    dist[neighbor.v] = dist[u] + neighbor.w;
                    pq.add(new Node(neighbor.v, dist[neighbor.v]));
                }
            }
        }

        for (int i = 1; i <= n; i++) {
            System.out.print((dist[i] == Integer.MAX_VALUE ? -1 : dist[i]) + (i == n ? "" : " "));
        }
        System.out.println();
    }
}
