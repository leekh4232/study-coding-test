class Solution {
    public int solution(int angle) {
        int answer = 0;

        if (angle < 90) {
            answer = 1; // 예각
        } else if (angle == 90) {
            answer = 2; // 직각
        } else if (angle < 180) {
            answer = 3; // 둔각
        } else {
            answer = 4; // 평각
        }

        return answer;
    }

    public static void main(String[] args) {
        Solution s = new Solution();

        // 테스트 예제 실행
        System.out.println(s.solution(70));  // 1
        System.out.println(s.solution(91));  // 3
        System.out.println(s.solution(180)); // 4
    }
}