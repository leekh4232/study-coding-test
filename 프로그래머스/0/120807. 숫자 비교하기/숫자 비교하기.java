class Solution {
    public int solution(int num1, int num2) {
        int answer = 0;

        if (num1 == num2) {
            answer = 1;
        } else {
            answer = -1;
        }

        return answer;
    }

    public static void main(String[] args) {
        Solution s = new Solution();

        // 테스트 예제 실행
        System.out.println(s.solution(2, 3));  // -1
        System.out.println(s.solution(11, 11)); // 1
        System.out.println(s.solution(7, 99));  // -1
    }
}