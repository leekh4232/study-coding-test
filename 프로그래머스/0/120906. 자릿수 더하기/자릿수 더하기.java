public class Solution {

    public static int solution(int n) {
        int sum = 0;

        // 1. 정수를 문자열로 변환하여 각 자리 문자 순회
        String str = String.valueOf(n);

        for (int i = 0; i < str.length(); i++) {
            char c = str.charAt(i);         // 각 문자 (예: '1')
            int digit = c - '0';            // 문자 → 정수 변환
            sum += digit;                   // 합계에 더하기
        }

        return sum;
    }

    // ✅ 테스트 실행
    public static void main(String[] args) {
        System.out.println(solution(1234));    // 10
        System.out.println(solution(930211));  // 16
    }
}
