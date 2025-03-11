import java.util.Arrays;

public class Solution {
    public int solution(int[] citations) {
        // 인용 횟수를 내림차순 정렬
        Arrays.sort(citations);
        int n = citations.length;

        // H-Index를 저장할 변수
        int answer = 0;

        // 정렬된 리스트를 순회하며 H-Index 계산
        for (int i = 0; i < n; i++) {
            int h = n - i; // 현재 논문의 인용 횟수가 (n-i)번 이상이면 조건 만족
            if (citations[i] >= h) {
                answer = h; // H-Index 업데이트
                break;
            }
        }

        // 최종 H-Index 반환
        return answer;
    }

    public static void main(String[] args) {
        Solution sol = new Solution();
        // ✅ 예제 테스트 실행
        System.out.println(sol.solution(new int[]{3, 0, 6, 1, 5})); // 결과: 3 (H-Index)
    }
}