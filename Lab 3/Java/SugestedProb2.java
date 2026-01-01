import java.util.*;

public class SugestedProb2 {
    static Map<String, Integer> mergeCount(Map<String, Integer> left, Map<String, Integer> right) {
        for (String key : right.keySet()) {
            left.put(key, left.getOrDefault(key, 0) + right.get(key));
        }
        return left;
    }

    static Map<String, Integer> divideCount(String[] words, int start, int end) {
        if (end - start == 1) {
            Map<String, Integer> map = new HashMap<>();
            map.put(words[start], 1);
            return map;
        }
        int mid = (start + end) / 2;
        Map<String, Integer> left = divideCount(words, start, mid);
        Map<String, Integer> right = divideCount(words, mid, end);
        return mergeCount(left, right);
    }

    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);
        if (!sc.hasNextInt())
            return;
        int n = sc.nextInt();
        String[] words = new String[n];
        for (int i = 0; i < n; i++)
            words[i] = sc.next();

        Map<String, Integer> freq = divideCount(words, 0, n);
        String maxWord = "";
        int maxCount = 0;
        for (String key : freq.keySet()) {
            if (freq.get(key) > maxCount) {
                maxCount = freq.get(key);
                maxWord = key;
            }
        }
        System.out.println(maxWord);
    }
}
