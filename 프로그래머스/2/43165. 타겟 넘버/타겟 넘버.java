class Solution {
    // 백트래킹을 통해 모든 경우의 수를 탐색하는 함수 정의
    public int backtrack(int[] numbers, int target, int idx, int currentSum) {
        // 모든 숫자를 사용한 경우 (재귀 종료 조건)
        if (idx == numbers.length) {
            // 현재까지의 합이 타겟과 일치하면 유효한 경우이므로 1을 반환
            if (currentSum == target) {
                return 1;
            }
            // 일치하지 않으면 유효하지 않은 경우이므로 0을 반환
            else {
                return 0;
            }
        }

        // 현재 숫자를 더한 경우를 재귀 호출
        int left = backtrack(numbers, target, idx + 1, currentSum + numbers[idx]);

        // 현재 숫자를 뺀 경우를 재귀 호출
        int right = backtrack(numbers, target, idx + 1, currentSum - numbers[idx]);

        // 두 경우를 더하여 현재 상태에서 가능한 전체 경우의 수를 반환
        return left + right;
    }

    // 문제 해결을 위한 메인 함수 정의
    public int solution(int[] numbers, int target) {
        // 인덱스 0부터 시작하고 현재 합은 0에서 출발
        return backtrack(numbers, target, 0, 0);
    }

    // 테스트용 코드
    public static void main(String[] args) {
        Solution sol = new Solution();
        // 예제 1: [1, 1, 1, 1, 1]로 3 만들기 (가능한 경우의 수: 5)
        System.out.println(sol.solution(new int[]{1, 1, 1, 1, 1}, 3));

        // 예제 2: [4, 1, 2, 1]로 4 만들기 (가능한 경우의 수: 2)
        System.out.println(sol.solution(new int[]{4, 1, 2, 1}, 4));
    }
}