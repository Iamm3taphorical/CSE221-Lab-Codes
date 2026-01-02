import java.util.*;
import java.io.*;

public class ProblemB {
    static int[] p;
    static int[] rank;

    static int find(int a) {
        while (p[a] != a) {
            p[a] = p[p[a]];
            a = p[a];
        }
        return a;
    }

    static class Edge implements Comparable<Edge> {
        int u, v, w;
        Edge(int u, int v, int w) {
            this.u = u;
            this.v = v;
            this.w = w;
        }
        public int compareTo(Edge other) {
            return Integer.compare(this.w, other.w);
        }
    }

    public static void main(String[] args) throws IOException {
        Scanner sc = new Scanner(System.in);
        if (!sc.hasNextInt()) return;
        int N = sc.nextInt();
        int M = sc.nextInt();
        List<Edge> edges = new ArrayList<>();
        for (int i = 0; i < M; i++) {
            int u = sc.nextInt();
            int v = sc.nextInt();
            int w = sc.nextInt();
            edges.add(new Edge(u, v, w));
        }
        Collections.sort(edges);

        p = new int[N + 1];
        rank = new int[N + 1];
        for (int i = 0; i <= N; i++) p[i] = i;

        long ans = 0;
        for (Edge e : edges) {
            int pu = find(e.u);
            int pv = find(e.v);
            if (pu != pv) {
                ans += e.w;
                if (rank[pu] < rank[pv]) {
                    int temp = pu; pu = pv; pv = temp;
                }
                p[pv] = pu;
                if (rank[pu] == rank[pv]) rank[pu]++;
            }
        }
        System.out.println(ans);
    }
}
