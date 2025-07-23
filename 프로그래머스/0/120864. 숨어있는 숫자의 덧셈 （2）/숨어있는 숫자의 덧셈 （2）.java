public class Solution {
    public static int solution(String my_string) {
        int answer = 0;
        int n = my_string.length();
        int i = 0;

        while (i < n) {
            String tmp = "";

            // 연속된 숫자 추출
            while (i < n) {
                char ch = my_string.charAt(i);
                if (Character.isDigit(ch)) {
                    tmp += ch;
                    i++;
                } else {
                    break;
                }
            }

            // 숫자가 존재하면 정수로 변환하여 합산
            if (!tmp.isEmpty()) {
                answer += Integer.parseInt(tmp);
            }

            // 다음 문자로 이동
            i++;
        }

        return answer;
    }

    // ✅ 예제 테스트 실행
    public static void main(String[] args) {
        System.out.println(solution("aAb1B2cC34oOp"));    // 37
        System.out.println(solution("1a2b3c4d123Z"));     // 133
    }
}
