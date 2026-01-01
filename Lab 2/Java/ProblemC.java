import java.util.*;

public class ProblemC {
    static class Pair implements Comparable<Pair> {
        int val, idx;

        public Pair(int v, int i) {
            val = v;
            idx = i;
        }

        public int compareTo(Pair o) {
            return Integer.compare(this.val, o.val);
        }
    }

    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);
        if (!sc.hasNextInt())
            return;
        int n = sc.nextInt();
        int t = sc.nextInt();
        Pair[] arr = new Pair[n];
        for (int i = 0; i < n; i++) {
            arr[i] = new Pair(sc.nextInt(), i + 1);
        }
        Arrays.sort(arr);
        boolean found = false;
        for (int i = 0; i < n - 2; i++) {
            int target = t - arr[i].val;
            int l = i + 1;
            int r = n - 1;
            while (l < r) {
                int sum = arr[l].val + arr[r].val;
                if (sum == target) {
                    System.out.println(arr[i].idx + " " + arr[l].idx + " " + arr[r].idx);
                    found = true;
                    break;
                } else if (sum < target) {
                    l++;
                } else {
                    r--;
                }
            }
            if (found)
                break;
        }
        if (!found)
            System.out.println("-1");
    }
}
