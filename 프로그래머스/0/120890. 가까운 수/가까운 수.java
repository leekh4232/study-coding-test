import java.util.Arrays;

public class Solution {

    public static int solution(int[] array, int n) {
        Arrays.sort(array);  // 오름차순 정렬

        int minDiff = Integer.MAX_VALUE;
        int answer = 0;

        for (int num : array) {
            int diff = Math.abs(n - num);

            if (diff < minDiff) {
                minDiff = diff;
                answer = num;
            }
        }

        return answer;
    }

    // ✅ 테스트 실행
    public static void main(String[] args) {
        System.out.println(solution(new int[]{3, 10, 28}, 20)); // 28
        System.out.println(solution(new int[]{10, 11, 12}, 13)); // 12
        System.out.println(solution(new int[]{7, 4, 10, 2}, 5)); // 4
    }
}
