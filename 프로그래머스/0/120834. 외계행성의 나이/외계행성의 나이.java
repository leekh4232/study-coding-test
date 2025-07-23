public class Solution {

    public static String solution(int age) {
        StringBuilder answer = new StringBuilder();

        // 1. 나이를 문자열로 변환하여 각 자리 문자 순회
        String ageStr = String.valueOf(age);

        for (int i = 0; i < ageStr.length(); i++) {
            char digit = ageStr.charAt(i);
            // 2. '0'을 기준으로 문자 → 정수 → 알파벳 문자로 변환
            int num = digit - '0'; // 문자 '3' → 정수 3
            char ch = (char) (num + 'a'); // 0 → 'a', 1 → 'b', ...
            answer.append(ch);
        }

        return answer.toString();
    }

    // ✅ 테스트 실행
    public static void main(String[] args) {
        System.out.println(solution(23));   // cd
        System.out.println(solution(51));   // fb
        System.out.println(solution(100));  // baa
    }
}
