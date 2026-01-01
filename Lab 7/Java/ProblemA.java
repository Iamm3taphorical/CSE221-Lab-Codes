import java.util.*;

public class ProblemA {
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
        // Using strict line/token reading. The problem implies standard CP input.
        if (!sc.hasNextInt())
            return;
        int n = sc.nextInt();
        int m = sc.nextInt();
        int s = sc.nextInt();
        int d = sc.nextInt();

        // Input format in Python:
        // Reads lists of u, then v, then w?
        // Wait. ProblemA.py splits ALL input tokens.
        // Then reads u_list, then v_list, then w_list?
        // A: "data = sys.stdin.read().strip().split()"
        // "i_var < m_var: u_list.append(...)".
        // THEN "i_var < m_var: v_list.append(...)".
        // THEN "i_var < m_var: w_list.append(...)".
        // This is weird. It implies structured input where ALL U's come first, then ALL
        // V's, then ALL W's.
        // I must match this pattern.

        int[] us = new int[m];
        for (int i = 0; i < m; i++)
            us[i] = sc.nextInt() - 1;

        int[] vs = new int[m];
        for (int i = 0; i < m; i++)
            vs[i] = sc.nextInt() - 1;

        int[] ws = new int[m];
        for (int i = 0; i < m; i++)
            ws[i] = sc.nextInt();

        List<List<Node>> adj = new ArrayList<>();
        for (int i = 0; i < n; i++)
            adj.add(new ArrayList<>());

        for (int i = 0; i < m; i++) {
            adj.get(us[i]).add(new Node(vs[i], ws[i]));
        }

        long INF = (long) 1e18;
        long[] dist = new long[n];
        Arrays.fill(dist, INF);
        int[] parent = new int[n];
        Arrays.fill(parent, -1);

        dist[s - 1] = 0;
        PriorityQueue<Node> pq = new PriorityQueue<>();
        pq.add(new Node(s - 1, 0));

        while (!pq.isEmpty()) {
            Node curr = pq.poll();
            if (curr.w > dist[curr.v])
                continue;

            for (Node neighbor : adj.get(curr.v)) {
                if (dist[curr.v] + neighbor.w < dist[neighbor.v]) {
                    dist[neighbor.v] = dist[curr.v] + neighbor.w;
                    parent[neighbor.v] = curr.v;
                    pq.add(new Node(neighbor.v, dist[neighbor.v]));
                }
            }
        }

        if (dist[d - 1] == INF) {
            System.out.println("-1");
        } else {
            System.out.println(dist[d - 1]);
            List<Integer> path = new ArrayList<>();
            int cur = d - 1;
            while (cur != -1) {
                path.add(cur + 1);
                cur = parent[cur];
            }
            Collections.reverse(path);
            for (int i = 0; i < path.size(); i++) {
                System.out.print(path.get(i) + (i == path.size() - 1 ? "" : " "));
            }
            System.out.println();
        }
    }
}
