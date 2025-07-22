public class Solution {

    public static String solution(String my_string) {
        StringBuilder answer = new StringBuilder();

        // 문자열을 한 글자씩 검사
        for (int i = 0; i < my_string.length(); i++) {
            char c = my_string.charAt(i);
            if (c != 'a' && c != 'e' && c != 'i' && c != 'o' && c != 'u') {
                answer.append(c);  // 모음이 아니면 추가
            }
        }

        return answer.toString();
    }

    // ✅ 테스트 실행
    public static void main(String[] args) {
        System.out.println(solution("bus"));              // 출력: bs
        System.out.println(solution("nice to meet you")); // 출력: nc t mt y
    }
}
