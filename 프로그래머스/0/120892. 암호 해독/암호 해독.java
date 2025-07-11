class Solution {
    public String solution(String cipher, int code) {
        String result = ""; // 결과를 저장할 문자열 초기화

        // code의 배수 번째 위치에 있는 문자만 추가
        for (int i = code - 1; i < cipher.length(); i += code) {
            result += cipher.charAt(i); // 해당 위치의 문자 추가
        }

        return result; // 최종 해독된 문자열 반환
    }

    public static void main(String[] args) {
        Solution sol = new Solution();

        // 테스트 예제 실행
        System.out.println(sol.solution("dfjardstddetckdaccccdegk", 4)); // "attack"
        System.out.println(sol.solution("pfqallllabwaoclk", 2)); // "fallback"
    }
}
