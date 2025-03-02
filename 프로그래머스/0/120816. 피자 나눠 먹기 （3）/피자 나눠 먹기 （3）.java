public class Solution {
    public int solution(int slice, int n) {
        // 기본적으로 필요한 피자 판 수
        int answer = n / slice;

        // n이 slice로 나누어 떨어지지 않는 경우
        if (n % slice != 0) {
            // 추가로 한 판을 더 주문해야 모든 사람이 먹을 수 있음
            answer++;
        }

        // 최종적으로 필요한 피자 판 수 반환
        return answer;
    }

    public static void main(String[] args) {
        Solution s = new Solution();
        System.out.println(s.solution(7, 10));
        System.out.println(s.solution(4, 12));
    }
}