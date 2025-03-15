class Solution {
    public int solution(String myString) {
        int answer = 0; // 숫자의 합을 저장할 변수

        // 문자열의 각 문자를 순회
        for (char m : myString.toCharArray()) {
            if (Character.isDigit(m)) { // 숫자인 경우
                answer += Character.getNumericValue(m); // 정수로 변환하여 더함
            }
        }

        return answer; // 최종 결과 반환
    }

    // 테스트 예제 실행
    public static void main(String[] args) {
        Solution sol = new Solution();
        System.out.println(sol.solution("aAb1B2cC34oOp")); // 10
        System.out.println(sol.solution("1a2b3c4d123")); // 16
    }
}
