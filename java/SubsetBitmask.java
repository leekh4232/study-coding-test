import java.util.*;

public class SubsetBitmask {
    public static void main(String[] args) {
        int[] arr = {1, 2, 3};
        int n = arr.length;

        for (int i = 0; i < (1 << n); i++) { // 0부터 2^n - 1까지
            List<Integer> subset = new ArrayList<>();

            for (int j = 0; j < n; j++) {
                if ((i & (1 << j)) != 0) {  // j번째 비트가 켜져 있는가?
                    subset.add(arr[j]);
                }
            }

            System.out.println(subset);
        }
    }
}
