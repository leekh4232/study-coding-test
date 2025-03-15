class Solution {
    public int solution(int num, int k) {
        String numStr = String.valueOf(num); // num을 문자열로 변환
        int index = numStr.indexOf(String.valueOf(k)); // k의 위치 찾기

        if (index != -1) {
            return index + 1; // 0-based index를 1-based로 변환하여 반환
        } else {
            return -1; // k가 포함되지 않으면 -1 반환
        }
    }

    // 테스트 예제 실행
    public static void main(String[] args) {
        Solution sol = new Solution();
        System.out.println(sol.solution(29183, 1)); // 3
        System.out.println(sol.solution(232443, 4)); // 4
        System.out.println(sol.solution(123456, 7)); // -1
    }
}
