import java.util.*;

public class Assignment2 {
    static void bfs(int start, List<List<Integer>> adj, int[] dist, int[] parent) {
        Arrays.fill(dist, -1);
        Queue<Integer> q = new LinkedList<>();
        dist[start] = 0;
        q.add(start);
        parent[start] = 0; // Using 0 as null-equivalent since 1-based indexing
        while (!q.isEmpty()) {
            int u = q.poll();
            for (int v : adj.get(u)) {
                if (dist[v] == -1) {
                    dist[v] = dist[u] + 1;
                    parent[v] = u;
                    q.add(v);
                }
            }
        }
    }

    static List<Integer> pathFinder(int dest, int src, int[] parent) {
        List<Integer> path = new ArrayList<>();
        int cur = dest;
        while (cur != 0) {
            path.add(cur);
            if (cur == src)
                break;
            cur = parent[cur];
        }
        Collections.reverse(path);
        return path;
    }

    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);
        if (!sc.hasNextInt())
            return;
        int n = sc.nextInt();
        int m = sc.nextInt();
        int source = sc.nextInt();
        int dest = sc.nextInt();
        int mandatory = sc.nextInt();

        List<List<Integer>> adj = new ArrayList<>();
        for (int i = 0; i <= n; i++)
            adj.add(new ArrayList<>());

        for (int i = 0; i < m; i++) {
            int u = sc.nextInt();
            int v = sc.nextInt();
            adj.get(u).add(v);
        }

        int[] distS = new int[n + 1];
        int[] parentS = new int[n + 1];
        bfs(source, adj, distS, parentS);

        if (distS[mandatory] == -1) {
            System.out.println("-1");
        } else {
            int[] distM = new int[n + 1];
            int[] parentM = new int[n + 1];
            bfs(mandatory, adj, distM, parentM);

            if (distM[dest] == -1) {
                System.out.println("-1");
            } else {
                List<Integer> part1 = pathFinder(mandatory, source, parentS);
                List<Integer> part2 = pathFinder(dest, mandatory, parentM);

                List<Integer> finalPath = new ArrayList<>(part1);
                // Remove first element of part2 (which is mandatory) to avoid duplicate
                if (part2.size() > 1) {
                    finalPath.addAll(part2.subList(1, part2.size()));
                } else if (part2.size() == 1 && part1.get(part1.size() - 1) != part2.get(0)) {
                    // This case shouldn't happen if mandatory is in both
                    finalPath.addAll(part2);
                }

                System.out.println(finalPath.size() - 1);
                for (int i = 0; i < finalPath.size(); i++) {
                    System.out.print(finalPath.get(i) + (i == finalPath.size() - 1 ? "" : " "));
                }
                System.out.println();
            }
        }
    }
}
