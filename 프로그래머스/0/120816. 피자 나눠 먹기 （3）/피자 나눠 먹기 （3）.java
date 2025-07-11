class Solution {
    public int solution(int slice, int n) {
        int answer = n / slice; // 기본적으로 필요한 피자 판 수 계산

        if (n % slice != 0) { // 나머지가 있으면 한 판 추가
            answer++;
        }

        return answer; // 최종적으로 필요한 피자 판 수 반환
    }

    public static void main(String[] args) {
        Solution s = new Solution();

        // 테스트 예제 실행
        System.out.println(s.solution(7, 10)); // 2
        System.out.println(s.solution(4, 12)); // 3
    }
}
