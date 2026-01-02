import java.util.*;
import java.io.*;

public class Problem1 {
    static int[] parent;
    static int[] sz;

    static int find(int x) {
        while (parent[x] != x) {
            parent[x] = parent[parent[x]];
            x = parent[x];
        }
        return x;
    }

    public static void main(String[] args) throws IOException {
        Scanner sc = new Scanner(System.in);
        if (!sc.hasNextInt())
            return;
        int N = sc.nextInt();
        int K = sc.nextInt();
        parent = new int[N + 1];
        sz = new int[N + 1];
        for (int i = 1; i <= N; i++) {
            parent[i] = i;
            sz[i] = 1;
        }

        PrintWriter pw = new PrintWriter(System.out);
        for (int i = 0; i < K; i++) {
            int a = sc.nextInt();
            int b = sc.nextInt();
            int pa = find(a);
            int pb = find(b);

            if (pa != pb) {
                if (sz[pa] < sz[pb]) {
                    int temp = pa;
                    pa = pb;
                    pb = temp;
                }
                parent[pb] = pa;
                sz[pa] += sz[pb];
            }
            pw.println(sz[find(a)]);
        }
        pw.flush();
    }
}
