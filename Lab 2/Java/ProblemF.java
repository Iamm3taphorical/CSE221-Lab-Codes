import java.util.Scanner;

public class ProblemF {
    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);
        if (!sc.hasNextInt())
            return;
        int n = sc.nextInt();
        int k = sc.nextInt();
        int[] a = new int[n];
        for (int i = 0; i < n; i++)
            a[i] = sc.nextInt();

        int[] freq = new int[100005]; // Adjust size as needed, using basic map assumption or array if elements small
        // Wait, element constraints? Python uses [0]*(n+1). Let's assume elements <= n
        // or similar.
        // Or use HashMap. Python code used array size n+1. So elements <= n.
        if (n > 100000)
            freq = new int[n + 100];
        else
            freq = new int[200000]; // Safe size

        int l = 0, r = 0, distinct = 0, maxMx = 0;

        while (r < n) {
            int curr = a[r];
            if (curr >= freq.length) { // Resize if needed
                // This shouldn't happen based on python code logic unless input large
            }
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
