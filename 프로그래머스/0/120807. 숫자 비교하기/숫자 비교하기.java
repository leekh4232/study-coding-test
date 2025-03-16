class Solution {
    public int solution(int num1, int num2) {
        return (num1 == num2) ? 1 : -1; // 삼항 연산자로 두 값 비교
    }

    public static void main(String[] args) {
        Solution s = new Solution();

        // 테스트 예제 실행
        System.out.println(s.solution(2, 3));  // -1
        System.out.println(s.solution(11, 11)); // 1
        System.out.println(s.solution(7, 99));  // -1
    }
}
