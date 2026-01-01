import java.util.*;

public class SugestedProb3 {
    static List<Integer> mergeZero(List<Integer> left, List<Integer> right) {
        List<Integer> merged = new ArrayList<>();
        List<Integer> combined = new ArrayList<>();
        combined.addAll(left);
        combined.addAll(right);
        for (int val : combined) {
            if (val != 0)
                merged.add(val);
        }
        for (int val : combined) {
            if (val == 0)
                merged.add(val);
        }
        return merged;
    }

    static List<Integer> divideZero(int[] arr, int start, int end) {
        if (end - start <= 1) {
            List<Integer> list = new ArrayList<>();
            if (end > start)
                list.add(arr[start]);
            return list;
        }
        int mid = (start + end) / 2;
        List<Integer> left = divideZero(arr, start, mid);
        List<Integer> right = divideZero(arr, mid, end);
        return mergeZero(left, right);
    }

    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);
        if (!sc.hasNextInt())
            return;
        int n = sc.nextInt();
        int[] arr = new int[n];
        for (int i = 0; i < n; i++)
            arr[i] = sc.nextInt();
        List<Integer> res = divideZero(arr, 0, n);
        for (int val : res)
            System.out.print(val + " ");
        System.out.println();
    }
}
