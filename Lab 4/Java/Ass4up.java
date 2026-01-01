import java.util.*;

public class Ass4up {
    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);
        if (!sc.hasNextInt())
            return;
        int t = sc.nextInt();
        while (t-- > 0) {
            if (!sc.hasNext())
                break;

            // Input format in Python: "temp_var = input().split(); vertices =
            // int(temp_var[0])..."
            // Java scanner handles whitespace.
            int n = sc.nextInt();
            int m = sc.nextInt();

            int[] starts = new int[m];
            for (int i = 0; i < m; i++)
                starts[i] = sc.nextInt();

            int[] ends = new int[m];
            for (int i = 0; i < m; i++)
                ends[i] = sc.nextInt();

            int[] degree = new int[n];
            for (int i = 0; i < m; i++) {
                degree[starts[i] - 1]++;
                degree[ends[i] - 1]++;
            }

            int odd = 0;
            for (int d : degree) {
                if (d % 2 != 0)
                    odd++;
            }

            if (odd == 0 || odd == 2)
                System.out.println("YES");
            else
                System.out.println("NO");
        }
    }
}
