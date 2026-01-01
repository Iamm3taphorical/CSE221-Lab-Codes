import java.util.*;

public class ProblemE {
    static class State implements Comparable<State> {
        int u;
        long dist;
        int lastPar;

        public State(int u, long dist, int lastPar) {
            this.u = u;
            this.dist = dist;
            this.lastPar = lastPar;
        }

        public int compareTo(State other) {
            return Long.compare(this.dist, other.dist);
        }
    }

    static class Edge {
        int v;
        int w;

        public Edge(int v, int w) {
            this.v = v;
            this.w = w;
        }
    }

    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);
        if (!sc.hasNextInt())
            return;
        int n = sc.nextInt();
        int m = sc.nextInt();

        // ProblemE.py:
        // Reads lists u_list, v_list, w_list (like ProblemA).
        int[] us = new int[m];
        for (int i = 0; i < m; i++)
            us[i] = sc.nextInt() - 1;

        int[] vs = new int[m];
        for (int i = 0; i < m; i++)
            vs[i] = sc.nextInt() - 1;

        int[] ws = new int[m];
        for (int i = 0; i < m; i++)
            ws[i] = sc.nextInt();

        List<List<Edge>> adj = new ArrayList<>();
        for (int i = 0; i < n; i++)
            adj.add(new ArrayList<>());

        for (int i = 0; i < m; i++) {
            adj.get(us[i]).add(new Edge(vs[i], ws[i]));
        }

        long INF = (long) 1e18;
        long[][] dist = new long[n][2];
        for (int i = 0; i < n; i++)
            Arrays.fill(dist[i], INF);

        PriorityQueue<State> pq = new PriorityQueue<>();
        dist[0][0] = 0; // Does parity imply 0 or 1? Python: dist[0][0] = 0; dist[0][1] = 0.
        // But what is the starting parity state? "last_par = -1".
        // It pushes (0, 0, -1).

        // Python code handles dist[0][0] = 0.
        // And dist[0][1] = 0?
        // Wait, Python code:
        // dist[0][0] = 0
        // dist[0][1] = 0
        // heapq.heappush(pq, (0, 0, -1))

        // This means we can start with any parity conceptually?
        // Or rather, the initial state has no parity restriction.
        // We track distance to node 'u' ending with edge parity 'p'.
        // But start node has no incoming edge.
        // Python logic allows moving from start to neighbors regardless of parity, and
        // sets the parity for next step.

        // Actually, Python initializes dist table at Start so subsequent visits are
        // pruned if larger.

        pq.add(new State(0, 0, -1));

        while (!pq.isEmpty()) {
            State curr = pq.poll();
            // We don't check `curr.dist > dist[curr.u][?]` easily because lastPar is -1.
            // If lastPar != -1, we check dist[u][lastPar].

            // Wait, Python doesn't check `visited` explicitly at pop.
            // It just iterates.
            // Efficiency issue? Maybe. But let's follow logic.

            for (Edge e : adj.get(curr.u)) {
                int par = e.w % 2;
                if (curr.lastPar != -1 && par == curr.lastPar)
                    continue;

                long nd = curr.dist + e.w;
                if (nd < dist[e.v][par]) {
                    dist[e.v][par] = nd;
                    pq.add(new State(e.v, nd, par));
                }
            }
        }

        long ans = Math.min(dist[n - 1][0], dist[n - 1][1]);
        System.out.println(ans == INF ? -1 : ans);
    }
}
