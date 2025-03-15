class Solution {
    public String solution(String myString) {
        String result = ""; // 결과 문자열 초기화

        // 문자열 순회하며 중복되지 않은 문자만 추가
        for (char c : myString.toCharArray()) {
            if (result.indexOf(c) == -1) { // 현재 문자가 결과 문자열에 없는 경우
                result += c; // 결과 문자열에 추가
            }
        }

        return result;
    }

    public static void main(String[] args) {
        Solution sol = new Solution();

        // 테스트 예제 실행
        System.out.println(sol.solution("people")); // "peol"
        System.out.println(sol.solution("We are the world")); // "We arthwold"
    }
}
