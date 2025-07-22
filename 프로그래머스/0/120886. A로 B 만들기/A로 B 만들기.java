public class Solution {

    public static int solution(String before, String after) {
        int answer = 1;

        for (int i = 0; i < before.length(); i++) {
            char c = before.charAt(i);
            int idx = after.indexOf(c);

            if (idx == -1) {
                answer = 0;
                break;
            }

            // after에서 해당 문자 제거 (중복 방지)
            after = after.substring(0, idx) + after.substring(idx + 1);
        }

        return answer;
    }

    // ✅ 테스트 실행
    public static void main(String[] args) {
        System.out.println(solution("olleh", "hello"));  // 1
        System.out.println(solution("allpe", "apple"));  // 1
        System.out.println(solution("apple", "applf"));  // 0
    }
}
