import java.util.*;

public class ProblemD {
    static class Node implements Comparable<Node> {
        int v;
        long w;

        public Node(int v, long w) {
            this.v = v;
            this.w = w;
        }

        public int compareTo(Node other) {
            return Long.compare(this.w, other.w);
        }
    }

    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);
        if (!sc.hasNextInt())
            return;
        int n = sc.nextInt();
        int m = sc.nextInt();
        int s = sc.nextInt() - 1;
        int d = sc.nextInt() - 1;

        // ProblemD.py:
        // Reads n weights for nodes.
        // Then m edges (u, v).

        int[] nodeWeights = new int[n];
        for (int i = 0; i < n; i++)
            nodeWeights[i] = sc.nextInt();

        List<List<Integer>> adj = new ArrayList<>();
        for (int i = 0; i < n; i++)
            adj.add(new ArrayList<>());

        for (int i = 0; i < m; i++) {
            int u = sc.nextInt() - 1;
            int v = sc.nextInt() - 1;
            adj.get(u).add(v);
        }

        long INF = (long) 1e18;
        long[] dist = new long[n];
        Arrays.fill(dist, INF);
        dist[s] = nodeWeights[s];

        PriorityQueue<Node> pq = new PriorityQueue<>();
        pq.add(new Node(s, dist[s]));

        while (!pq.isEmpty()) {
            Node curr = pq.poll();
            if (curr.w > dist[curr.v])
                continue;

            for (int v : adj.get(curr.v)) {
                long nd = curr.w + nodeWeights[v]; // Cost is sum of node weights visited
                if (nd < dist[v]) {
                    dist[v] = nd;
                    pq.add(new Node(v, nd));
                }
            }
        }

        System.out.println(dist[d] == INF ? -1 : dist[d]);
    }
}
