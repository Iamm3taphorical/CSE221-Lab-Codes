import java.util.*;

public class SugestedProb13 {
    static List<Integer> solve(List<Integer> in, List<Integer> pre) {
        if (in.isEmpty())
            return new ArrayList<>();
        int root = pre.get(0);
        int idx = in.indexOf(root);

        List<Integer> leftIn = in.subList(0, idx);
        List<Integer> rightIn = in.subList(idx + 1, in.size());

        List<Integer> leftPre = pre.subList(1, 1 + leftIn.size());
        List<Integer> rightPre = pre.subList(1 + leftIn.size(), pre.size());

        List<Integer> left = solve(leftIn, leftPre);
        List<Integer> right = solve(rightIn, rightPre);

        List<Integer> res = new ArrayList<>();
        res.addAll(left);
        res.addAll(right);
        res.add(root);
        return res;
    }

    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);
        if (!sc.hasNextInt())
            return;
        int n = sc.nextInt();
        List<Integer> in = new ArrayList<>();
        for (int i = 0; i < n; i++)
            in.add(sc.nextInt());
        List<Integer> pre = new ArrayList<>();
        for (int i = 0; i < n; i++)
            pre.add(sc.nextInt());

        List<Integer> res = solve(in, pre);
        for (int val : res)
            System.out.print(val + " ");
        System.out.println();
    }
}
