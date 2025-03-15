class Solution {
    public String solution(String myString) {
        String result = "";  // 변환된 문자열을 저장할 변수

        // 문자열의 각 문자를 순회하며 변환
        for (int i = 0; i < myString.length(); i++) {
            String currentChar = myString.substring(i, i + 1);  // 현재 문자 가져오기
            
            // 대문자인 경우 소문자로 변환, 소문자인 경우 대문자로 변환
            if (currentChar.equals(currentChar.toUpperCase())) {  
                result += currentChar.toLowerCase();  // 대문자를 소문자로 변환
            } else {
                result += currentChar.toUpperCase();  // 소문자를 대문자로 변환
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
