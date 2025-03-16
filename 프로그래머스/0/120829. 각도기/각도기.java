class Solution {
    public int solution(int angle) {
        if (angle < 90) return 1; // 예각
        if (angle == 90) return 2; // 직각
        if (angle < 180) return 3; // 둔각
        return 4; // 평각
    }

    public static void main(String[] args) {
        Solution s = new Solution();
        
        // 테스트 예제 실행
        System.out.println(s.solution(70));  // 1
        System.out.println(s.solution(91));  // 3
        System.out.println(s.solution(180)); // 4
    }
}
