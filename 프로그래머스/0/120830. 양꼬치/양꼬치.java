public class Solution {
    public int solution(int n, int k) {
        int answer = 12000 * n + 2000 * (k - n / 10);
        return answer;
    }

    public static void main(String[] args) {
        Solution s = new Solution();
        System.out.println(s.solution(10, 3));
        System.out.println(s.solution(64, 6));
    }
}