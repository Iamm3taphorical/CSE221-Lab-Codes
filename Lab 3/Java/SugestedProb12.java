import java.util.*;

public class SugestedProb12 {
    static List<Integer> getInorder(List<Integer> pre, List<Integer> post) {
        if (pre.isEmpty())
            return new ArrayList<>();
        int root = pre.get(0);
        if (pre.size() == 1) {
            List<Integer> res = new ArrayList<>();
            res.add(root);
            return res;
        }
        int leftRoot = pre.get(1);
        int k = post.indexOf(leftRoot);
        int leftSize = k + 1;

        List<Integer> leftPre = pre.subList(1, 1 + leftSize);
        List<Integer> rightPre = pre.subList(1 + leftSize, pre.size());

        List<Integer> leftPost = post.subList(0, leftSize);
        List<Integer> rightPost = post.subList(leftSize, post.size() - 1);

        List<Integer> left = getInorder(leftPre, leftPost);
        List<Integer> right = getInorder(rightPre, rightPost);

        List<Integer> res = new ArrayList<>();
        res.addAll(left);
        res.add(root);
        res.addAll(right);
        return res;
    }

    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);
        if (!sc.hasNextInt())
            return;
        int n = sc.nextInt();
        List<Integer> pre = new ArrayList<>();
        for (int i = 0; i < n; i++)
            pre.add(sc.nextInt());
        List<Integer> post = new ArrayList<>();
        for (int i = 0; i < n; i++)
            post.add(sc.nextInt());

        List<Integer> res = getInorder(pre, post);
        for (int val : res)
            System.out.print(val + " ");
        System.out.println();
    }
}
