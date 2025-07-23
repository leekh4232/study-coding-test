import java.util.*;

public class Solution {
    public static int[] solution(int[] emergency) {
        int[] sorted_em = emergency.clone();
        Arrays.sort(sorted_em);  // 오름차순 정렬
        // 내림차순으로 보기 위해 뒤집어서 순위 계산
        int[] answer = new int[emergency.length];

        for (int i = 0; i < emergency.length; i++) {
            for (int j = sorted_em.length - 1; j >= 0; j--) {
                if (emergency[i] == sorted_em[j]) {
                    answer[i] = sorted_em.length - j;
                    break;
                }
            }
        }

        return answer;
    }

    // ✅ 예제 테스트 실행
    public static void main(String[] args) {
        System.out.println(Arrays.toString(solution(new int[]{3, 76, 24})));         // [3, 1, 2]
        System.out.println(Arrays.toString(solution(new int[]{1, 2, 3, 4, 5, 6, 7}))); // [7, 6, 5, 4, 3, 2, 1]
        System.out.println(Arrays.toString(solution(new int[]{30, 10, 23, 6, 100}))); // [2, 4, 3, 5, 1]
    }
}
