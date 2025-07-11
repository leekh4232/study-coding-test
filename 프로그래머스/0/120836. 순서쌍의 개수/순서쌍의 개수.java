class Solution {
    public int solution(int n) {
        int count = 0; // 순서쌍 개수를 저장할 변수 초기화

        // 1부터 n까지 반복하면서 약수 개수 카운트
        for (int i = 1; i <= n; i++) {
            if (n % i == 0) { // i가 n의 약수인지 확인
                count++; // 약수이면 순서쌍 개수 증가
            }
        }

        return count; // 최종적으로 구한 순서쌍 개수 반환
    }

    public static void main(String[] args) {
        Solution sol = new Solution();

        // 테스트 예제 실행
        System.out.println(sol.solution(20)); // 6
        System.out.println(sol.solution(100)); // 9
    }
}
