import java.util.*;

public class ProblemB {
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

    static long[] dijkstra(int start, List<List<Node>> adj, int n) {
        long INF = (long) 1e18;
        long[] dist = new long[n];
        Arrays.fill(dist, INF);
        dist[start] = 0;
        PriorityQueue<Node> pq = new PriorityQueue<>();
        pq.add(new Node(start, 0));

        while (!pq.isEmpty()) {
            Node curr = pq.poll();
            if (curr.w > dist[curr.v])
                continue;
            for (Node neighbor : adj.get(curr.v)) {
                if (dist[curr.v] + neighbor.w < dist[neighbor.v]) {
                    dist[neighbor.v] = dist[curr.v] + neighbor.w;
                    pq.add(new Node(neighbor.v, dist[neighbor.v]));
                }
            }
        }
        return dist;
    }

    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);
        if (!sc.hasNextInt())
            return;
        int n = sc.nextInt();
        int m = sc.nextInt();
        int a = sc.nextInt() - 1;
        int b = sc.nextInt() - 1;

        // ProblemB.py reads: u, v, w sequentially in loop.
        // "i_var < m_var: u = ... v = ... w = ..."
        // This is simpler structure.

        List<List<Node>> adj = new ArrayList<>();
        for (int i = 0; i < n; i++)
            adj.add(new ArrayList<>());

        for (int i = 0; i < m; i++) {
            int u = sc.nextInt() - 1;
            int v = sc.nextInt() - 1;
            int w = sc.nextInt();
            adj.get(u).add(new Node(v, w));
        }

        long[] distA = dijkstra(a, adj, n);
        long[] distB = dijkstra(b, adj, n);

        long INF = (long) 1e18;
        long bestTime = INF;
        int bestNode = -1;

        for (int i = 0; i < n; i++) {
            if (distA[i] != INF && distB[i] != INF) {
                long meetTime = Math.max(distA[i], distB[i]);
                if (meetTime < bestTime) {
                    bestTime = meetTime;
                    bestNode = i;
                } else if (meetTime == bestTime) {
                    if (bestNode == -1 || i < bestNode)
                        bestNode = i;
                }
            }
        }

        if (bestNode == -1)
            System.out.println("-1");
        else
            System.out.println(bestTime + " " + (bestNode + 1));
    }
}
