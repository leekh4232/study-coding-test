class Solution {
    public String solution(String cipher, int code) {
        // 결과를 저장할 StringBuilder 객체 초기화
        StringBuilder answer = new StringBuilder();

        // code의 배수 번째 위치에 있는 문자만 추가
        for (int i = code - 1; i < cipher.length(); i += code) {
            answer.append(cipher.charAt(i));
        }

        // 최종 해독된 문자열 반환
        return answer.toString();
    }

    public static void main(String[] args) {
        Solution sol = new Solution();

        // 테스트 예제 실행
        System.out.println(sol.solution("dfjardstddetckdaccccdegk", 4)); // "attack"
        System.out.println(sol.solution("pfqallllabwaoclk", 2)); // "fallback"
    }
}
