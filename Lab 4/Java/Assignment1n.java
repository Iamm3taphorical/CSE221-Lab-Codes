import java.util.*;

public class Assignment1n {
    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);
        if (!sc.hasNextInt())
            return;
        int n = sc.nextInt();
        int m = sc.nextInt();

        List<List<Integer>> adj = new ArrayList<>();
        for (int i = 0; i <= n; i++)
            adj.add(new ArrayList<>());

        for (int i = 0; i < m; i++) {
            int u = sc.nextInt();
            int v = sc.nextInt();
            adj.get(u).add(v);
            adj.get(v).add(u);
        }

        int[] visited = new int[n + 1];
        List<Integer> bfsOrder = new ArrayList<>();
        Queue<Integer> q = new LinkedList<>();

        visited[1] = 1;
        q.add(1);

        while (!q.isEmpty()) {
            int u = q.poll();
            bfsOrder.add(u);

            for (int v : adj.get(u)) {
                if (visited[v] == 0) {
                    visited[v] = 1;
                    q.add(v);
                }
            }
        }

        for (int i = 0; i < bfsOrder.size(); i++) {
            System.out.print(bfsOrder.get(i) + (i == bfsOrder.size() - 1 ? "" : " "));
        }
        System.out.println();
    }
}
