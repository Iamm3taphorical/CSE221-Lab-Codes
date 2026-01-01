import java.util.*;

public class ProblemA1 {
    static long inversions = 0;

    static int[] merge(int[] a, int[] b) {
        int[] c = new int[a.length + b.length];
        int i = 0, j = 0, k = 0;
        long inv = 0;
        while (i < a.length && j < b.length) {
            if (a[i] > b[j]) {
                c[k++] = b[j++];
                inv += (a.length - i);
            } else {
                c[k++] = a[i++];
            }
        }
        while (i < a.length)
            c[k++] = a[i++];
        while (j < b.length)
            c[k++] = b[j++];
        inversions += inv;
        return c;
    }

    static int[] mergeSort(int[] arr) {
        if (arr.length <= 1)
            return arr;
        int mid = arr.length / 2;
        int[] left = Arrays.copyOfRange(arr, 0, mid);
        int[] right = Arrays.copyOfRange(arr, mid, arr.length);
        int[] sortedLeft = mergeSort(left);
        int[] sortedRight = mergeSort(right);
        System.out.println(Arrays.toString(sortedLeft) + " " + Arrays.toString(sortedRight));
        int[] result = merge(sortedLeft, sortedRight);
        System.out.println(Arrays.toString(result));
        return result;
    }

    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);
        if (!sc.hasNextInt())
            return;
        int n = sc.nextInt();
        int[] arr = new int[n];
        for (int i = 0; i < n; i++)
            arr[i] = sc.nextInt();
        int[] res = mergeSort(arr);
        System.out.println(inversions);
        for (int val : res)
            System.out.print(val + " ");
        System.out.println();
    }
}
