import java.util.*;
import java.io.*;

public class ProblemF {
    static class Task implements Comparable<Task> {
        int a, d;

        Task(int a, int d) {
            this.a = a;
            this.d = d;
        }

        public int compareTo(Task other) {
            return Integer.compare(this.a, other.a);
        }
    }

    public static void main(String[] args) throws IOException {
        Scanner sc = new Scanner(System.in);
        if (!sc.hasNextInt())
            return;
        int n = sc.nextInt();
        Task[] tasks = new Task[n];
        for (int i = 0; i < n; i++) {
            tasks[i] = new Task(sc.nextInt(), sc.nextInt());
        }
        Arrays.sort(tasks);

        long t = 0;
        long reward = 0;
        for (Task task : tasks) {
            t += task.a;
            reward += task.d - t;
        }
        System.out.println(reward);
    }
}
