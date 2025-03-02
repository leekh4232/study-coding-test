public class Solution {
    public int solution(int num1, int num2) {
        // 일단 두 수가 같다고 가정
        int answer = 1;

        // 두 수가 다르면 -1로 변경
        if (num1 != num2) {
            answer = -1;
        }

        return answer;
    }

    public static void main(String[] args) {
        Solution s = new Solution();
        System.out.println(s.solution(2, 3));
        System.out.println(s.solution(11, 11));
        System.out.println(s.solution(7, 9));
    }
}