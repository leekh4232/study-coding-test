public class Solution {
    public static String solution(String my_string) {
        String answer = "";

        // 각 글자를 배열로 분리
        char[] cArr = my_string.toCharArray();

        // 문자열의 각 문자를 순회하며 변환
        for (char c : cArr) {
            int k = (int) c;

            // 아스키코드에 의한 대문자
            if (k >= 65 && k <= 96) {
                answer += (char)(k + 32);
            } else {
                answer += (char)(k - 32);
            }
        }

        return answer;
    }

    public static void main(String[] args) {
        System.out.println(solution("cccCCC"));       // CCCccc
        System.out.println(solution("abCdEfghIJ"));   // ABcDeFGHij
    }
}
