public class Solution {
    public static int solution(String my_string) {
        int answer = 0;

        for (char m : my_string.toCharArray()) {
            int code = (int)m;
            if (code >= 48 && code <= 57) {
                answer += (code - 48);
            }
        }

        return answer;
    }

    public static void main(String[] args) {
        System.out.println(solution("aAb1B2cC34oOp"));
    }
}