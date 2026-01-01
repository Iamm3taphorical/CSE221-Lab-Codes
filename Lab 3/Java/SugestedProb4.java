import java.util.Scanner;

public class SugestedProb4 {
    static class Pair {
        int odd, even;

        Pair(int o, int e) {
            odd = o;
            even = e;
        }
    }

    static Pair countOddEven(int[] arr, int start, int end) {
        if (end - start == 1) {
            if (arr[start] % 2 == 0)
                return new Pair(0, 1);
            else
                return new Pair(1, 0);
        }
        int mid = (start + end) / 2;
        Pair left = countOddEven(arr, start, mid);
        Pair right = countOddEven(arr, mid, end);
        return new Pair(left.odd + right.odd, left.even + right.even);
    }

    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);
        if (!sc.hasNextInt())
            return;
        int n = sc.nextInt();
        int[] arr = new int[n];
        for (int i = 0; i < n; i++)
            arr[i] = sc.nextInt();
        Pair res = countOddEven(arr, 0, n);
        System.out.println(res.odd + " " + res.even);
    }
}
