import java.util.*;

public class Solution {
    public int[] solution(int[] arr) {
        int sum = 0;
        for (int i=0; i<arr.length; i++) {
            sum += arr[i];
        }

        int[] answer = new int[sum];

        int idx = 0;
        for (int i=0; i<arr.length; i++) {
            for (int j=0; j<arr[i]; j++) {
                answer[idx+j] = arr[i];
            }
            idx += arr[i];
        }

        return answer;
    }

    public static void main(String[] args) {
        Solution sol = new Solution();
        System.out.println(Arrays.toString(sol.solution(new int[]{5, 1, 4})));
        System.out.println(Arrays.toString(sol.solution(new int[]{6, 6})));
        System.out.println(Arrays.toString(sol.solution(new int[]{1})));
    }
}