class Solution {
    public int solution(int n) {
        int answer = 1; // 최소 피자 판 수 초기화

        // 최소한의 피자 판 수를 찾을 때까지 반복
        while ((answer * 6) % n != 0) {
            answer++; // 조건을 만족할 때까지 answer 증가
        }

        return answer; // 계산된 최소 피자 판 수 반환
    }

    public static void main(String[] args) {
        Solution sol = new Solution();

        // 테스트 예제 실행
        System.out.println(sol.solution(6));  // 1
        System.out.println(sol.solution(10)); // 5
        System.out.println(sol.solution(4));  // 2
    }
}
