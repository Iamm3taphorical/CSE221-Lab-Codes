import java.util.*;

public class Assignment7 {
    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);
        if (!sc.hasNextInt())
            return;
        int n = sc.nextInt();
        String[] words = new String[n];
        for (int i = 0; i < n; i++)
            words[i] = sc.next();

        List<Set<Integer>> adj = new ArrayList<>();
        for (int i = 0; i < 26; i++)
            adj.add(new HashSet<>());

        int[] inDegree = new int[26];
        boolean[] present = new boolean[26];

        for (String w : words) {
            for (char c : w.toCharArray())
                present[c - 'a'] = true;
        }

        for (int i = 0; i < n - 1; i++) {
            String w1 = words[i];
            String w2 = words[i + 1];
            int len = Math.min(w1.length(), w2.length());
            boolean diffFound = false;

            for (int k = 0; k < len; k++) {
                if (w1.charAt(k) != w2.charAt(k)) {
                    int u = w1.charAt(k) - 'a';
                    int v = w2.charAt(k) - 'a';
                    if (!adj.get(u).contains(v)) {
                        adj.get(u).add(v);
                        inDegree[v]++;
                    }
                    diffFound = true;
                    break;
                }
            }
            if (!diffFound && w1.length() > w2.length()) {
                System.out.println("-1"); // Invalid order
                return;
            }
        }

        PriorityQueue<Integer> pq = new PriorityQueue<>(); // Lexicographically smallest first
        for (int i = 0; i < 26; i++) {
            if (present[i] && inDegree[i] == 0)
                pq.add(i);
        }

        StringBuilder sb = new StringBuilder();
        int count = 0;
        int totalPresent = 0;
        for (boolean p : present)
            if (p)
                totalPresent++;

        while (!pq.isEmpty()) {
            int u = pq.poll();
            sb.append((char) ('a' + u));
            count++;

            for (int v : adj.get(u)) {
                inDegree[v]--;
                if (inDegree[v] == 0)
                    pq.add(v);
            }
        }

        if (count != totalPresent)
            System.out.println("-1");
        else
            System.out.println(sb.toString());
    }
}
