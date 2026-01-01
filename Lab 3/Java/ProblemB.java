import java.util.*;

public class ProblemB {
    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);
        if (!sc.hasNextInt())
            return;
        int n = sc.nextInt();
        List<Long> arr = new ArrayList<>();
        List<Long> sortedLeft = new ArrayList<>();
        long result = 0;

        for (int i = 0; i < n; i++) {
            long val = sc.nextLong();
            arr.add(val);
            long threshold = val * val;

            int idx = Collections.binarySearch(sortedLeft, threshold);
            if (idx < 0)
                idx = -(idx + 1);
            else {
                while (idx < sortedLeft.size() && sortedLeft.get(idx) <= threshold)
                    idx++;
            }
            // Logic check: python bisect_right returns insertion point after elements <=
            // threshold
            // Collections.binarySearch returns index or -(insertion point) - 1.
            // If found, may not be the last occurence. bisect_right is equivalent to
            // upper_bound.

            int uIdx = upperBound(sortedLeft, threshold);
            result += (sortedLeft.size() - uIdx);

            int insIdx = upperBound(sortedLeft, val);
            sortedLeft.add(insIdx, val);
        }
        System.out.println(result);
    }

    static int upperBound(List<Long> list, long val) {
        int l = 0, r = list.size();
        while (l < r) {
            int mid = l + (r - l) / 2;
            if (list.get(mid) <= val) {
                l = mid + 1;
            } else {
                r = mid;
            }
        }
        return l;
    }
}
