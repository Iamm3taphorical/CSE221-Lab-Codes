import java.util.*;

public class Assignment6 {
    static final int MAX = 5000;
    static List<Integer>[] pf = new ArrayList[MAX + 1];

    static void sieve() {
        boolean[] isPrime = new boolean[MAX + 1];
        Arrays.fill(isPrime, true);
        isPrime[0] = isPrime[1] = false;

        for (int i = 2; i * i <= MAX; i++) {
            if (isPrime[i]) {
                for (int j = i * i; j <= MAX; j += i) {
                    isPrime[j] = false;
                }
            }
        }

        for (int i = 2; i <= MAX; i++) {
            pf[i] = new ArrayList<>();
            int temp = i;
            for (int x = 2; x * x <= temp; x++) {
                if (temp % x == 0) {
                    if (isPrime[x])
                        pf[i].add(x);
                    while (temp % x == 0)
                        temp /= x;
                }
            }
            if (temp > 1 && isPrime[temp])
                pf[i].add(temp);
        }
    }

    public static void main(String[] args) {
        sieve();
        Scanner sc = new Scanner(System.in);
        if (!sc.hasNextInt())
            return;
        int t = sc.nextInt();
        while (t-- > 0) {
            int s = sc.nextInt();
            int tx = sc.nextInt();

            if (s == tx) {
                System.out.println(0);
                continue;
            }

            int[] dist = new int[MAX + 1];
            Arrays.fill(dist, -1);
            Queue<Integer> q = new LinkedList<>();

            dist[s] = 0;
            q.add(s);

            int ans = -1;

            while (!q.isEmpty()) {
                int u = q.poll();
                if (pf[u] != null) {
                    for (int p : pf[u]) {
                        int nxt = u + p;
                        if (nxt <= tx && dist[nxt] == -1) {
                            dist[nxt] = dist[u] + 1;
                            if (nxt == tx) {
                                ans = dist[nxt];
                                break;
                            }
                            q.add(nxt);
                        }
                    }
                }
                if (ans != -1)
                    break;
            }

            System.out.println(ans);
        }
    }
}
