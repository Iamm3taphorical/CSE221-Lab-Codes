import java.io.*;
import java.util.*;

public class ProblemC {
    static int[] parent, rank_;
    static List<int[]>[] adj;
    static int N;

    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        StringTokenizer st = new StringTokenizer(br.readLine());

        N = Integer.parseInt(st.nextToken());
        int M = Integer.parseInt(st.nextToken());

        int[][] edges = new int[M][3];
        for (int i = 0; i < M; i++) {
            st = new StringTokenizer(br.readLine());
            edges[i][0] = Integer.parseInt(st.nextToken()); // u
            edges[i][1] = Integer.parseInt(st.nextToken()); // v
            edges[i][2] = Integer.parseInt(st.nextToken()); // w
        }

        // Sort edges by weight
        Arrays.sort(edges, (a, b) -> a[2] - b[2]);

        // Initialize Union-Find
        parent = new int[N + 1];
        rank_ = new int[N + 1];
        for (int i = 0; i <= N; i++) {
            parent[i] = i;
            rank_[i] = 0;
        }

        // Build MST using Kruskal's
        long mstCost = 0;
        List<int[]> mstEdges = new ArrayList<>();
        List<int[]> nonMstEdges = new ArrayList<>();
        int mstEdgeCount = 0;

        for (int[] edge : edges) {
            int u = edge[0], v = edge[1], w = edge[2];
            if (union(u, v)) {
                mstCost += w;
                mstEdges.add(new int[] { u, v, w });
                mstEdgeCount++;
            } else {
                nonMstEdges.add(new int[] { u, v, w });
            }
        }

        // Check if MST exists
        if (mstEdgeCount != N - 1) {
            System.out.println(-1);
            return;
        }

        // Build adjacency list for MST
        adj = new ArrayList[N + 1];
        for (int i = 0; i <= N; i++) {
            adj[i] = new ArrayList<>();
        }
        for (int[] edge : mstEdges) {
            int u = edge[0], v = edge[1], w = edge[2];
            adj[u].add(new int[] { v, w });
            adj[v].add(new int[] { u, w });
        }

        // Find second best MST
        long secondBest = Long.MAX_VALUE;

        for (int[] edge : nonMstEdges) {
            int u = edge[0], v = edge[1], w = edge[2];
            int maxEdge = findMaxEdge(u, v);
            if (maxEdge < w) {
                long candidate = mstCost - maxEdge + w;
                secondBest = Math.min(secondBest, candidate);
            }
        }

        if (secondBest == Long.MAX_VALUE) {
            System.out.println(-1);
        } else {
            System.out.println(secondBest);
        }
    }

    static int find(int x) {
        if (parent[x] != x) {
            parent[x] = find(parent[x]);
        }
        return parent[x];
    }

    static boolean union(int x, int y) {
        int px = find(x), py = find(y);
        if (px == py)
            return false;
        if (rank_[px] < rank_[py]) {
            int temp = px;
            px = py;
            py = temp;
        }
        parent[py] = px;
        if (rank_[px] == rank_[py]) {
            rank_[px]++;
        }
        return true;
    }

    static int findMaxEdge(int src, int dst) {
        // BFS to find max edge on path
        boolean[] visited = new boolean[N + 1];
        int[] parentNode = new int[N + 1];
        int[] edgeWeight = new int[N + 1];

        Queue<Integer> queue = new LinkedList<>();
        queue.offer(src);
        visited[src] = true;
        parentNode[src] = -1;

        while (!queue.isEmpty()) {
            int node = queue.poll();
            if (node == dst) {
                // Trace back to find max edge
                int maxEdge = 0;
                int curr = dst;
                while (parentNode[curr] != -1) {
                    maxEdge = Math.max(maxEdge, edgeWeight[curr]);
                    curr = parentNode[curr];
                }
                return maxEdge;
            }

            for (int[] neighbor : adj[node]) {
                int next = neighbor[0], weight = neighbor[1];
                if (!visited[next]) {
                    visited[next] = true;
                    parentNode[next] = node;
                    edgeWeight[next] = weight;
                    queue.offer(next);
                }
            }
        }

        return -1; // Should not happen
    }
}
