class Solution {
    public String solution(String myString, int n) {
        String result = "";  // 결과를 저장할 문자열 초기화

        // myString의 각 문자를 순회
        for (int i = 0; i < myString.length(); i++) {
            String currentChar = myString.substring(i, i + 1);  // 현재 문자 추출
            
            // 현재 문자를 n번 반복하여 추가
            for (int j = 0; j < n; j++) {
                result += currentChar;
            }
        }

        return result;  // 최종 변환된 문자열 반환
    }

    // 테스트 코드
    public static void main(String[] args) {
        Solution sol = new Solution();
        System.out.println(sol.solution("hello", 3));  // "hhheeellllllooo"
    }
}
