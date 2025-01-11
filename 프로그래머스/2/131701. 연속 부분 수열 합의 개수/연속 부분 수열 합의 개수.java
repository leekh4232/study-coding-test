/**
 * 프로그래머스 131701 - 연속 부분 수열 합의 개수
 * https://school.programmers.co.kr/learn/courses/30/lessons/
 */
import java.util.HashSet;
import java.util.Set;

 public class Solution {
    public int solution(int[] elements) {
        int answer = 0;
        Set<Integer> res = new HashSet<>(); // 결과를 저장할 집합 (중복 제거)
        int n = elements.length;           // 수열의 길이

        // 원형 수열을 처리하기 위해 배열 두 배 확장
        int[] ext = new int[n * 2];
        for (int i = 0; i < n; i++) {
            ext[i] = elements[i];
            ext[i + n] = elements[i];
        }

        // 모든 길이에 대해 반복
        for (int length = 1; length <= n; length++) {
            int winSum = 0;

            // 슬라이딩 윈도우 초기 합 계산
            for (int i = 0; i < length; i++) {
                winSum += ext[i];
            }
            res.add(winSum);

            // 슬라이딩 윈도우 이동
            for (int i = 1; i < n; i++) {
                winSum = winSum - ext[i - 1] + ext[i + length - 1];
                res.add(winSum);
            }
        }

        answer = res.size();
        return answer; // 중복을 제거한 연속 부분 수열 합의 개수를 반환
    }

    public static void main(String[] args) {
        Solution sol = new Solution();
        System.out.println(sol.solution(new int[]{7, 9, 1, 1, 4})); // 18
    }
}