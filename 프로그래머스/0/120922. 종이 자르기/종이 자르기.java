public class Solution {
    public int solution(int M, int N) {
        return (M - 1) + M * (N - 1);
    }

    public static void main(String[] args) {
        Solution s = new Solution();
        System.out.println(s.solution(2, 2));
        System.out.println(s.solution(2, 5));
        System.out.println(s.solution(1, 1));
    }
}