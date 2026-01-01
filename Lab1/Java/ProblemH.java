import java.util.*;

public class ProblemH {
    static class Train {
        String name;
        int time;
        int idx;
        String line;

        public Train(String n, int t, int i, String l) {
            name = n;
            time = t;
            idx = i;
            line = l;
        }
    }

    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);
        if (!sc.hasNextLine())
            return;
        String line1 = sc.nextLine();
        if (line1.isEmpty())
            return;
        int n = Integer.parseInt(line1.trim());
        Train[] trains = new Train[n];
        for (int i = 0; i < n; i++) {
            String line = sc.nextLine().trim();
            String[] parts = line.split("\\s+");
            String name = parts[0];
            String timeStr = parts[parts.length - 1];
            String[] timeParts = timeStr.split(":");
            int hr = Integer.parseInt(timeParts[0]);
            int mn = Integer.parseInt(timeParts[1]);
            int totalTime = hr * 60 + mn;
            trains[i] = new Train(name, totalTime, i, line);
        }
        for (int i = 0; i < n; i++) {
            for (int j = 0; j < n - 1; j++) {
                boolean swap = false;
                if (trains[j].name.compareTo(trains[j + 1].name) > 0)
                    swap = true;
                else if (trains[j].name.equals(trains[j + 1].name)) {
                    if (trains[j].time < trains[j + 1].time)
                        swap = true;
                }
                if (swap) {
                    Train tmp = trains[j];
                    trains[j] = trains[j + 1];
                    trains[j + 1] = tmp;
                }
            }
        }
        for (int i = 0; i < n; i++)
            System.out.println(trains[i].line);
    }
}
