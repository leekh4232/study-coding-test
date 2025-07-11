class Solution {
    public int solution(String message) {
        // 문자열의 길이를 구한 후 각 문자당 2cm를 곱하여 반환
        return message.length() * 2;
    }

    public static void main(String[] args) {
        Solution sol = new Solution();

        // 테스트 예제 실행
        System.out.println(sol.solution("happy birthday!")); // 30
        System.out.println(sol.solution("I love you~")); // 22
    }
}
