import java.util.*;

public class Assignment2 {
    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);
        if (!sc.hasNextInt())
            return;
        int n = sc.nextInt();
        int m = sc.nextInt();

        // Reading lists of starts, ends, weights
        // Python code reads all starts, then all ends, then all weights.
        // Wait, input format in Python:
        // "start_var = list(map(int , input().split()))"
        // "end_var = list(map(int , input().split()))"
        // "weight_var = list(map(int , input().split()))"

        int[] starts = new int[m];
        for (int i = 0; i < m; i++)
            starts[i] = sc.nextInt();

        int[] ends = new int[m];
        for (int i = 0; i < m; i++)
            ends[i] = sc.nextInt();

        int[] weights = new int[m];
        for (int i = 0; i < m; i++)
            weights[i] = sc.nextInt();

        List<List<String>> adj = new ArrayList<>();
        for (int i = 0; i < n; i++)
            adj.add(new ArrayList<>());

        for (int i = 0; i < m; i++) {
            int u = starts[i] - 1;
            int v = ends[i];
            int w = weights[i];
            adj.get(u).add("(" + v + ", " + w + ")"); // String format to match Python print "(dest, weight)"
            // Python output: print(str(x_var + 1) + ":", *adjList_var[x_var])
            // Python tuple printing: (v, w)
            // Java manually format used.
        }

        for (int i = 0; i < n; i++) {
            System.out.print((i + 1) + " :");
            for (String s : adj.get(i)) {
                System.out.print(" " + s);
            }
            System.out.println();
        }
    }
}
