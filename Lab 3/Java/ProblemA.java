import java.util.Scanner;

public class ProblemA {
    static long invCount = 0;

    static int[] merge(int[] a, int[] b) {
        int[] merged = new int[a.length + b.length];
        int i = 0, j = 0, k = 0;
        while (i < a.length && j < b.length) {
            if (a[i] <= b[j]) {
                merged[k++] = a[i++];
            } else {
                merged[k++] = b[j++];
                invCount += (a.length - i);
            }
        }
        while (i < a.length)
            merged[k++] = a[i++];
        while (j < b.length)
            merged[k++] = b[j++];
        return merged;
    }

    static int[] mergeSort(int[] arr) {
        if (arr.length <= 1)
            return arr;
        int mid = arr.length / 2;
        int[] left = new int[mid];
        int[] right = new int[arr.length - mid];
        System.arraycopy(arr, 0, left, 0, mid);
        System.arraycopy(arr, mid, right, 0, arr.length - mid);
        int[] leftSorted = mergeSort(left);
        int[] rightSorted = mergeSort(right);
        return merge(leftSorted, rightSorted);
    }

    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);
        if (!sc.hasNextInt())
            return;
        int n = sc.nextInt();
        int[] arr = new int[n];
        for (int i = 0; i < n; i++)
            arr[i] = sc.nextInt();
        int[] sorted = mergeSort(arr);
        System.out.println(invCount);
        for (int i = 0; i < n; i++)
            System.out.print(sorted[i] + " ");
        System.out.println();
    }
}
