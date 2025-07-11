class Solution {
    public String solution(String myString, String letter) {
        String result = ""; // 결과 문자열 초기화

        // 문자열 순회하며 letter와 다른 문자만 추가
        for (char c : myString.toCharArray()) {
            if (c != letter.charAt(0)) { // letter와 다른 문자만 추가
                result += c;
            }
        }

        return result; // 최종 변환된 문자열 반환
    }

    public static void main(String[] args) {
        Solution sol = new Solution();

        // 테스트 예제 실행
        System.out.println(sol.solution("abcdef", "f")); // "abcde"
        System.out.println(sol.solution("BCBdbe", "B")); // "Cdbe"
    }
}
