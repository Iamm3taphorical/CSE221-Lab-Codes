import java.util.Scanner;

public class SugestedProb7 {
    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);
        if (!sc.hasNextInt())
            return;
        int n = sc.nextInt();
        long[] a = new long[n];
        for (int i = 0; i < n; i++)
            a[i] = sc.nextLong();

        long bestSquare = a[0] * a[0];
        int bestI = 0;
        long maxVal = Long.MIN_VALUE;
        int bestJ = 1;

        for (int j = 1; j < n; j++) {
            long currentCube = a[j] * a[j] * a[j];
            long sum = bestSquare + currentCube;
            if (sum > maxVal) {
                maxVal = sum;
                bestJ = j;
            }
            if ((a[j] * a[j]) > bestSquare) {
                bestSquare = a[j] * a[j];
                bestI = j;
            }
        }
        // Wait, bestI needs to be the index corresponding to bestSquare used for
        // maxVal.
        // The Python logic: updates bestI after checking sum. So bestI refers to
        // previous best square.
        // But if maxVal updates, we need the CURRENT bestI.
        // Python code: DOES NOT TRACK bestI associated with maxVal?
        // It prints `best_i_var` and `best_j_var` at the end.
        // `best_i_var` is updated whenever `best_square_var` updates.
        // So `best_i_var` at the end is just the index of largest square in the whole
        // array (up to n-1).
        // This seems like a bug in the Python logic if it intends to print the pair
        // producing maxVal.
        // But "replicate" means copying logic.
        // However, I see `best_i_var` is updated. It stores the index of max square
        // seen so far.
        // The problem asks for Indices perhaps?
        // Actually, Python code prints `best_i_var` and `best_j_var`.
        // BUT `best_i_var` is the index of max square OVERALL, not necessarily the one
        // that contributed to `maxVal`.
        // UNLESS the problem asks for something else?
        // Actually, looking at Python logic:
        // updates maxVal/bestJ using CURRENT `best_square_var` (which comes from
        // `best_i_var` BEFORE update).
        // Then updates `best_square_var`/`best_i_var`.
        // So `best_i_var` tracks the running max square.
        // But wait, the printed `best_i_var` is merely the index of global max square.
        // I should stick to exact logic.
        // BUT `best_i_var` in Python code might be wrong?

        // Python Code:
        // while j < n:
        // sum = best_square + cube
        // if sum > max: max = sum, best_j = j
        // if square > best_square: best_square = square, best_i = j
        // print best_i, best_j

        // Note: It prints `best_i` (index of absolute max square) and `best_j` (index
        // of cube completing the max pair).
        // This pair (best_i, best_j) might NOT be the pair that sums to `max_val`!
        // Example: [100, 1]. Square(100)=10000. i=0. j=1. Sum=10000+1=10001. max=10001,
        // best_j=1. best_square=100, best_i=0.
        // Example: [1, 100]. j=1. Square(1)=1. Sum=1+1000000. max=1000001, best_j=1.
        // Then best_square=10000, best_i=1.
        // Output: 1 1. Pair is (100, 100)? No, logic says i < j.
        // Logic seems broken in Python code or I misunderstand the goal.
        // However, user said "replicate each and every solution".
        // I will copy the Java logic to match Python exactly.

        // But I need to define `bestI` outside to match Python state.
        // In Python, `best_i_var = 0` initially.
        // And it is updated.
        // I'll replicate.

        System.out.println(bestI + " " + bestJ);
    }
}
