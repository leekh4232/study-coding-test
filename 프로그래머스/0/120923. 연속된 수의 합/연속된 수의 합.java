import java.util.Arrays;

public class Solution {

    public static int[] solution(int num, int total) {
        int[] answer = new int[num];

        // 1. 첫 번째 숫자 계산
        int start = total / num - (num - 1) / 2;

        // 2. 연속된 숫자 채우기
        for (int i = 0; i < num; i++) {
            answer[i] = start + i;
        }

        return answer;
    }

    // ✅ 테스트 실행
    public static void main(String[] args) {
        System.out.println(Arrays.toString(solution(3, 12))); // [3, 4, 5]
        System.out.println(Arrays.toString(solution(5, 15))); // [1, 2, 3, 4, 5]
        System.out.println(Arrays.toString(solution(4, 14))); // [2, 3, 4, 5]
        System.out.println(Arrays.toString(solution(5, 5)));  // [-1, 0, 1, 2, 3]
    }
}
