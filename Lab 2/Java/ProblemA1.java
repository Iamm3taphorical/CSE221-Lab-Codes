import java.util.Scanner;

public class ProblemA1 {
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
        int left = 0;
        int right = n - 1;
        boolean found = false;
        while (left < right) {
            int sum = arr[left] + arr[right];
            if (sum == s) {
                System.out.println((left + 1) + " " + (right + 1));
                found = true;
                break;
            } else if (sum > s) {
                right--;
            } else {
                left++;
            }
        }
        if (!found) {
            System.out.println("-1");
        }
    }
}
