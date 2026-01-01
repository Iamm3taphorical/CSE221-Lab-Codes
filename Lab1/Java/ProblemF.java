import java.util.Scanner;

public class ProblemF {
    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);
        if (!sc.hasNextInt())
            return;
        int n = sc.nextInt();
        int[] arr = new int[n];
        for (int i = 0; i < n; i++)
            arr[i] = sc.nextInt();
        boolean swapFlag = true;
        while (swapFlag) {
            swapFlag = false;
            for (int i = 0; i < n - 1; i++) {
                if (arr[i] % 2 == arr[i + 1] % 2) {
                    if (arr[i] > arr[i + 1]) {
                        int temp = arr[i];
                        arr[i] = arr[i + 1];
                        arr[i + 1] = temp;
                        swapFlag = true;
                    }
                }
            }
        }
        for (int i = 0; i < n; i++)
            System.out.print(arr[i] + " ");
    }
}
