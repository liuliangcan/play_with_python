import java.io.BufferedInputStream;
import java.util.ArrayList;
import java.util.Arrays;
import java.util.Scanner;

public class Main {
    static Scanner scanner = new Scanner(new BufferedInputStream(System.in));

    public static ArrayList<Integer> get(int[] nums, int p) {
        ArrayList<Integer> ans = new ArrayList<>();
        if (p == 0) {
            return ans;
        }
        int nLen = nums.length;
        for (int i = 0; i < nLen; i++) {
            while (!ans.isEmpty() && ans.get(ans.size() - 1) < nums[i] && nLen - i + ans.size() > p) {
                ans.remove(ans.size() - 1);
            }
            ans.add(nums[i]);
        }
        return new ArrayList<>(ans.subList(0, p));
    }

    public static int compareList(ArrayList<Integer> list1, ArrayList<Integer> list2) {
        int size = Math.min(list1.size(), list2.size());
        for (int i = 0; i < size; i++) {
            if (list1.get(i) > list2.get(i)) {
                return 1;
            } else if (list1.get(i) < list2.get(i)) {
                return -1;
            }
        }
        return Integer.compare(list1.size(), list2.size());
    }

    public static void solve() {
        int m = scanner.nextInt();
        int n = scanner.nextInt();
        int[] a = new int[m];
        int[] b = new int[n];
        for (int i = 0; i < m; i++) {
            a[i] = scanner.nextInt();
        }
        for (int i = 0; i < n; i++) {
            b[i] = scanner.nextInt();
        }
        int k = scanner.nextInt();

        ArrayList<Integer> ans = new ArrayList<>();
        for (int x = Math.max(0, k - b.length); x <= Math.min(k, a.length); x++) {
            ArrayList<Integer> ans1 = get(a, x);
            ArrayList<Integer> ans2 = get(b, k - x);
            ArrayList<Integer> p = new ArrayList<>();
            int i = 0;
            int j = 0;
            while (i < x && j < k - x) {
                if (ans1.get(i) > ans2.get(j)) {
                    p.add(ans1.get(i));
                    i++;
                } else {
                    p.add(ans2.get(j));
                    j++;
                }
            }
            p.addAll(ans1.subList(i, ans1.size()));
            p.addAll(ans2.subList(j, ans2.size()));
            if (ans.isEmpty() || compareList(p, ans) > 0) {
                ans = p;
            }
        }

        StringBuilder result = new StringBuilder();
        for (int num : ans) {
            result.append(num).append(" ");
        }
        System.out.println(result.toString().trim());
    }

    public static void main(String[] args) {
        solve();
    }
}

