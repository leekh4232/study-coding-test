public class Solution {
    public int solution(int num1, int num2) {
        int answer = num1 + num2;
        return answer;
    }

    public static void main(String[] args) {
        Solution s = new Solution();
        System.out.println(s.solution(2, 3));
        System.out.println(s.solution(100, 2));
    }
}