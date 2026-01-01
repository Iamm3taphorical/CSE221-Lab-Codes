import java.util.*;

public class ProblemF {
    static List<Integer> arranger(List<Integer> arr) {
        if (arr.isEmpty())
            return new ArrayList<>();
        int mid = arr.size() / 2;
        int root = arr.get(mid);
        List<Integer> left = arranger(arr.subList(0, mid));
        List<Integer> right = arranger(arr.subList(mid + 1, arr.size()));
        List<Integer> res = new ArrayList<>();
        res.add(root);
        res.addAll(left);
        res.addAll(right);
        return res;
    }

    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);
        if (!sc.hasNextInt())
            return;
        int n = sc.nextInt();
        List<Integer> arr = new ArrayList<>();
        for (int i = 0; i < n; i++)
            arr.add(sc.nextInt());
        List<Integer> res = arranger(arr);
        for (int val : res)
            System.out.print(val + " ");
        System.out.println();
    }
}
