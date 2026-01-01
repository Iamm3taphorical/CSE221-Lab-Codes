import java.util.*;

public class ProblemE {
    static boolean isSorted(int[] arr) {
        for (int i = 0; i < arr.length - 1; i++) {
            if (arr[i] > arr[i + 1])
                return false;
        }
        return true;
    }

    static void reverse(int[] arr, int start, List<String> moves) {
        int left = start, right = start + 2;
        while (left < right) {
            int temp = arr[left];
            arr[left] = arr[right];
            arr[right] = temp;
            left++;
            right--;
        }
        moves.add((start + 1) + " " + (start + 3));
    }

    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);
        if (!sc.hasNextInt())
            return;
        int n = sc.nextInt();
        int[] arr = new int[n];
        for (int i = 0; i < n; i++)
            arr[i] = sc.nextInt();
        List<String> moves = new ArrayList<>();
        boolean done = false;
        if (n <= 2) {
            if (isSorted(arr)) {
                System.out.println("YES");
                System.out.println(0);
            } else {
                System.out.println("NO");
            }
        } else {
            int iter = 0;
            while (true) {
                boolean swapped = false;
                for (int i = 0; i <= n - 3; i++) {
                    if (arr[i] > arr[i + 1] || arr[i + 1] > arr[i + 2]) {
                        reverse(arr, i, moves);
                        swapped = true;
                    }
                }
                if (isSorted(arr)) {
                    done = true;
                    break;
                }
                if (!swapped)
                    break;
                iter++;
                if (iter > n * 2)
                    break;
            }
            if (done && isSorted(arr)) {
                System.out.println("YES");
                System.out.println(moves.size());
                for (String s : moves)
                    System.out.println(s);
            } else {
                System.out.println("NO");
            }
        }
    }
}
