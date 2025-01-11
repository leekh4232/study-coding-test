/**
 * 프로그래머스 131127 - 할인행사
 * https://school.programmers.co.kr/learn/courses/30/lessons/131127
 */

import java.util.HashMap;
import java.util.Map;

public class Solution {
    public int solution(String[] want, int[] num, String[] disc) {
        // 필요한 제품 목록과 수량을 딕셔너리로 변환
        Map<String, Integer> wantMap = new HashMap<>();
        for (int i = 0; i < want.length; i++) {
            wantMap.put(want[i], num[i]);
        }

        // 슬라이딩 윈도우 크기
        int winSize = 0;
        for (int n : num) {
            winSize += n;
        }

        int count = 0;

        // 슬라이딩 윈도우를 활용한 비교
        for (int i = 0; i <= disc.length - winSize; i++) {
            // 현재 윈도우 내 상품 수량 계산
            Map<String, Integer> winMap = new HashMap<>();
            for (int j = 0; j < winSize; j++) {
                String item = disc[i + j];
                winMap.put(item, winMap.getOrDefault(item, 0) + 1);
            }

            // 필요한 제품 수량 충족 여부 확인
            boolean allSatisfied = true;
            for (String item : wantMap.keySet()) {
                if (winMap.getOrDefault(item, 0) < wantMap.get(item)) {
                    allSatisfied = false;
                    break;
                }
            }

            if (allSatisfied) {
                count++;
            }
        }

        return count;
    }

    public static void main(String[] args) {
        Solution sol = new Solution();

        // 결과 --> 3
        System.out.println(sol.solution(
            new String[]{"banana", "apple", "rice", "pork", "pot"},
            new int[]{3, 2, 2, 2, 1},
            new String[]{"chicken", "apple", "apple", "banana", "rice",
                         "apple", "pork", "banana", "pork", "rice", "pot",
                         "banana", "apple", "banana"}));

        // 결과 --> 0
        System.out.println(sol.solution(
            new String[]{"apple"},
            new int[]{10},
            new String[]{"banana", "banana", "banana", "banana", "banana",
                         "banana", "banana", "banana", "banana", "banana"}));
    }
}