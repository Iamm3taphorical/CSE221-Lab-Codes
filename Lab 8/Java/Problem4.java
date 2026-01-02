import java.util.*;
import java.io.*;

public class Problem4 {
    static class Task implements Comparable<Task> {
        int s, e;

        Task(int s, int e) {
            this.s = s;
            this.e = e;
        }

        public int compareTo(Task other) {
            return Integer.compare(this.e, other.e);
        }
    }

    public static void main(String[] args) throws IOException {
        Scanner sc = new Scanner(System.in);
        if (!sc.hasNextInt())
            return;
        int N = sc.nextInt();
        Task[] tasks = new Task[N];
        for (int i = 0; i < N; i++) {
            tasks[i] = new Task(sc.nextInt(), sc.nextInt());
        }
        Arrays.sort(tasks);

        List<Task> res = new ArrayList<>();
        long last = Long.MIN_VALUE;

        for (Task t : tasks) {
            if (t.s > last) {
                res.add(t);
                last = t.e;
            }
        }

        System.out.println(res.size());
        for (Task t : res) {
            System.out.println(t.s + " " + t.e);
        }
    }
}
