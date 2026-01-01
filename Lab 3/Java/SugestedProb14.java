import java.util.*;

public class SugestedProb14 {
    static List<Integer> solve(List<Integer> in, List<Integer> post) {
        if (in.isEmpty())
            return new ArrayList<>();
        int root = post.get(post.size() - 1);
        int idx = in.indexOf(root);

        List<Integer> leftIn = in.subList(0, idx);
        List<Integer> rightIn = in.subList(idx + 1, in.size());

        List<Integer> leftPost = post.subList(0, leftIn.size());
        List<Integer> rightPost = post.subList(leftIn.size(), post.size() - 1);

        List<Integer> left = solve(leftIn, leftPost);
        List<Integer> right = solve(rightIn, rightPost);

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
        List<Integer> in = new ArrayList<>();
        for (int i = 0; i < n; i++)
            in.add(sc.nextInt());
        List<Integer> post = new ArrayList<>();
        for (int i = 0; i < n; i++)
            post.add(sc.nextInt());

        List<Integer> res = solve(in, post);
        for (int val : res)
            System.out.print(val + " ");
        System.out.println();
    }
}
