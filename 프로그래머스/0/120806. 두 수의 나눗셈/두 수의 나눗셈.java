public class Solution {
    public int solution(int num1, int num2) {
        return (int)((double) num1 / num2 * 1000);
    }

    public static void main(String[] args) {
        Solution s = new Solution();
        System.out.println(s.solution(10, 5));
        System.out.println(s.solution(7, 2));
    }
}