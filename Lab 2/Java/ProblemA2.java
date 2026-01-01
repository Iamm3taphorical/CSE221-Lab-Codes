import java.util.Scanner;

public class ProblemA2 {
    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);
        if (!sc.hasNextInt())
            return;
        int n = sc.nextInt();
        int s = sc.nextInt();
        int[] arr = new int[n];
        for (int i = 0; i < n; i++) {
            arr[i] = sc.nextInt();
        }
        int l = 0;
        int r = n - 1;
        boolean flag = false;
        while (l < r) {
            int sum = arr[l] + arr[r];
            if (sum == s) {
                System.out.println((l + 1) + " " + (r + 1));
                flag = true;
                break;
            } else if (sum > s) {
                r--;
            } else {
                l++;
            }
        }
        if (!flag) {
            System.out.println("-1");
        }
    }
}
