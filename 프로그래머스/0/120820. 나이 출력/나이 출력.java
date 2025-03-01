public class Solution {
    public int solution(int age) {
        int answer = 2022 - age + 1;
        return answer;
    }

    public static void main(String[] args) {
        Solution s = new Solution();
        System.out.println(s.solution(40));
        System.out.println(s.solution(23));
    }
}