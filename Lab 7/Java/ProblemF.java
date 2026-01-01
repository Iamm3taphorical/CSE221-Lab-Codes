import java.util.*;

public class ProblemF {
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
        long[] dist1 = new long[n];
        long[] dist2 = new long[n];
        Arrays.fill(dist1, INF);
        Arrays.fill(dist2, INF);

        dist1[s] = 0;
        PriorityQueue<Node> pq = new PriorityQueue<>();
        pq.add(new Node(s, 0));

        while (!pq.isEmpty()) {
            Node curr = pq.poll();
            int u = curr.v;
            long cost = curr.w;

            if (cost > dist2[u])
                continue; // Optimization: node visited with cost > 2nd best is useless

            for (Node neighbor : adj.get(u)) {
                long nd = cost + neighbor.w;

                if (nd < dist1[neighbor.v]) {
                    dist2[neighbor.v] = dist1[neighbor.v];
                    dist1[neighbor.v] = nd;
                    pq.add(new Node(neighbor.v, nd));
                    // Also push old best as candidate for 2nd best?
                    // Python code: "dist2[nxt] = dist1[nxt]; dist1[nxt] = nd; heappush(..., nd)"
                    // It pushes the NEW best.
                    // What about the OLD best? "dist2[nxt] = dist1[nxt]".
                    // Should we push updated dist2?
                    // Python doesn't push dist2 update here.
                    // But wait, if we update dist2, we should push it so it can propagate?
                    // Python code:
                    // if nd < dist1: update both, push NEW dist1.
                    // elif dist1 < nd < dist2: update dist2, push NEW dist2.
                    // It seems it relies on the fact that if we found a new best, we explore it.
                    // If we found a new 2nd best, we explore it.
                    // BUT, when updating dist2 from dist1 (in the first if), we do NOT push the old
                    // dist1 value as a new dist2 path.
                    // Is this correct?
                    // The old dist1 value was ALREADY pushed when it was set.
                    // So its extensions are already in queue or processed.
                    // So we don't need to re-push it.
                    // Correct.

                    // But wait, `heapq.heappush(pq, (nd, nxt))` inside the first block.
                    // This pushes the SHORTEST path.
                    // In the second block, it pushes the SECOND shortest.
                    // It seems correct.
                    // Wait, if `dist1` becomes `dist2`, that value (old dist1) represents a valid
                    // path length.
                    // Its edges were processed when it was dist1.
                    // Do we need to process them again as dist2?
                    // Yes, because extensions from a second-shortest path might form
                    // second-shortest paths to neighbors.
                    // The Python code DOES NOT push the `dist2` value in the first block.
                    // Only pushes `nd` (new dist1).
                    // This might be a logic flaw in the Python reference?
                    // Or maybe it is sufficient.
                    // Actually, usually in K-th shortest path, if we shift valid values down, we
                    // might need to re-push.
                    // But I must blindly follow Python code provided by user.
                    // Python code:
                    /*
                     * if nd < dist1[nxt]:
                     * dist2[nxt] = dist1[nxt]
                     * dist1[nxt] = nd
                     * heapq.heappush(pq, (nd, nxt))
                     * elif dist1[nxt] < nd < dist2[nxt]:
                     * dist2[nxt] = nd
                     * heapq.heappush(pq, (nd, nxt))
                     */
                    // I will replicate this EXACTLY.
                    pq.add(new Node(neighbor.v, /* dist2 was updated but we push */ nd));
                    // Wait. In block 1, we push `nd`. `nd` is `dist1`.
                    // In block 2, we push `nd`. `nd` is `dist2`.
                    // So we push `nd` in both cases.

                    // Wait, if I replicate Python logic:
                    // `heapq.heappush(pq, (nd, nxt))` is called in both branches.
                    // I will do the same.

                    // Actually, in Java `pq.add(new Node(neighbor.v, nd))` is sufficient.
                } else if (cost + neighbor.w < dist2[neighbor.v] && cost + neighbor.w > dist1[neighbor.v]) {
                    dist2[neighbor.v] = cost + neighbor.w;
                    pq.add(new Node(neighbor.v, dist2[neighbor.v]));
                }
            }
        }

        System.out.println(dist2[d] == INF ? -1 : dist2[d]);
    }
}
