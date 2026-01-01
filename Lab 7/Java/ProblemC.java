import java.util.*;

public class ProblemC {
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

        // ProblemC.py reads u, v, w sequentially.

        List<List<Node>> adj = new ArrayList<>();
        for (int i = 0; i < n; i++)
            adj.add(new ArrayList<>());

        for (int i = 0; i < m; i++) {
            int u = sc.nextInt() - 1;
            int v = sc.nextInt() - 1;
            int w = sc.nextInt();
            adj.get(u).add(new Node(v, w));
            adj.get(v).add(new Node(u, w));
        }

        long INF = (long) 1e18;
        long[] danger = new long[n];
        Arrays.fill(danger, INF);
        danger[0] = 0;

        PriorityQueue<Node> pq = new PriorityQueue<>();
        pq.add(new Node(0, 0));

        while (!pq.isEmpty()) {
            Node curr = pq.poll();
            if (curr.w > danger[curr.v])
                continue;

            for (Node neighbor : adj.get(curr.v)) {
                long nd = Math.max(curr.w, neighbor.w);
                if (nd < danger[neighbor.v]) {
                    danger[neighbor.v] = nd;
                    pq.add(new Node(neighbor.v, nd));
                }
            }
        }

        for (int i = 0; i < n; i++) {
            System.out.print((danger[i] == INF ? -1 : danger[i]) + (i == n - 1 ? "" : " "));
        }
        System.out.println();
    }
}
