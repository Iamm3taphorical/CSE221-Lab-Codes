import java.util.Scanner;

public class ProblemF1 {
    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);
        if (!sc.hasNextInt())
            return;
        int n = sc.nextInt();
        int k = sc.nextInt();
        int[] a = new int[n];
        for (int i = 0; i < n; i++)
            a[i] = sc.nextInt();

        int[] freq = new int[200005];
        int l = 0, r = 0, distinct = 0, maxMx = 0;

        while (r < n) {
            int curr = a[r];
            if (curr >= freq.length) {
            } // Safety
            if (freq[curr] == 0)
                distinct++;
            freq[curr]++;

            while (distinct > k) {
                int leftVal = a[l];
                freq[leftVal]--;
                if (freq[leftVal] == 0)
                    distinct--;
                l++;
            }
            int win = r - l + 1;
            if (win > maxMx)
                maxMx = win;
            r++;
        }
        System.out.println(maxMx);
    }
}
