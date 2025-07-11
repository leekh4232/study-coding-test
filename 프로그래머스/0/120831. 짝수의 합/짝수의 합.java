class Solution {
    public int solution(int n) {
        int sum = 0; // 짝수들의 합을 저장할 변수 초기화

        // 1부터 n까지 반복하며 짝수인 경우만 합산
        for (int i = 1; i <= n; i++) {
            if (i % 2 == 0) { // 짝수인지 확인
                sum += i; // 짝수일 경우 합산
            }
        }

        return sum; // 최종적으로 누적된 짝수의 합 반환
    }

    public static void main(String[] args) {
        Solution sol = new Solution();

        // 테스트 예제 실행
        System.out.println(sol.solution(10)); // 30
        System.out.println(sol.solution(4));  // 6
    }
}
