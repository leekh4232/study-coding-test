import java.util.*;

public class Solution {

    public static int[] solution(int n, int[] numlist) {
        List<Integer> result = new ArrayList<>();

        for (int num : numlist) {
            if (num % n == 0) {
                result.add(num);
            }
        }

        // List<Integer> → int[]로 변환
        int[] answer = new int[result.size()];
        for (int i = 0; i < result.size(); i++) {
            answer[i] = result.get(i);
        }

        return answer;
    }

    // ✅ 테스트 실행
    public static void main(String[] args) {
        System.out.println(Arrays.toString(solution(3, new int[]{4, 5, 6, 7, 8, 9, 10, 11, 12})));
        // 출력: [6, 9, 12]
    }
}
