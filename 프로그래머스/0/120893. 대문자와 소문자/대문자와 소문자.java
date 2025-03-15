class Solution {
    public String solution(String myString) {
        String result = "";  // 변환된 문자열을 저장할 변수

        // 문자열의 각 문자를 순회하며 변환
        for (char c : myString.toCharArray()) {
            if (Character.isUpperCase(c)) {  // 현재 문자가 대문자인 경우
                result += Character.toLowerCase(c);  // 소문자로 변환하여 추가
            } else {  // 현재 문자가 소문자인 경우
                result += Character.toUpperCase(c);  // 대문자로 변환하여 추가
            }
        }

        return result;  // 변환된 문자열 반환
    }

    // 테스트 코드
    public static void main(String[] args) {
        Solution sol = new Solution();
        System.out.println(sol.solution("cccCCC"));       // CCCccc
        System.out.println(sol.solution("abCdEfghIJ"));   // ABcDeFGHij
    }
}