import java.util.HashSet;
import java.util.Set;

public class Solution {
    public int solution(int[] elements) {
        int answer = 0;
        Set<Integer> res = new HashSet<>(); // 결과를 저장할 집합 (중복 제거)
        int n = elements.length;           // 원형 수열의 길이

        // 원형 수열을 처리하기 위해 배열을 두 배 확장
        int[] ext = new int[n * 2]; // 두 배 크기의 배열 생성
        for (int i = 0; i < n; i++) {
            ext[i] = elements[i];    // 원본 배열 복사
            ext[i + n] = elements[i]; // 뒤쪽에 한 번 더 추가하여 원형 구조를 표현
        }

        // 가능한 모든 길이의 부분 수열 탐색
        for (int length = 1; length <= n; length++) { // 부분 수열의 길이를 1부터 n까지 설정
            int winSum = 0; // 현재 윈도우 내의 합

            // 초기 슬라이딩 윈도우 합 계산
            for (int i = 0; i < length; i++) {
                winSum += ext[i]; // 첫 length개의 합 계산
            }
            res.add(winSum); // 집합에 추가하여 중복 제거

            // 슬라이딩 윈도우를 한 칸씩 이동하며 부분합 계산
            for (int i = 1; i < n; i++) { // 원본 배열의 길이만큼 반복
                winSum = winSum - ext[i - 1] + ext[i + length - 1]; // 첫 원소 제거 후 새 원소 추가
                res.add(winSum); // 새로운 합을 집합에 추가
            }
        }

        answer = res.size(); // 중복을 제거한 부분 수열 합의 개수 계산
        return answer; // 결과 반환
    }

    public static void main(String[] args) {
        Solution sol = new Solution();
        System.out.println(sol.solution(new int[]{7, 9, 1, 1, 4})); // 18
    }
}
