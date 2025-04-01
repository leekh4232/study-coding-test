public class Solution {
    public static String solution(String my_string, int n) {
        String answer = "";

        // 각 글자를 배열로 분리
        char[] cArr = my_string.toCharArray();

        // 문자열의 각 문자를 순회하며 변환
        for (char c : cArr) {
            for (int i=0; i<n; i++) {
                answer += c;
            }
        }

        return answer;
    }

    public static void main(String[] args) {
        System.out.println(solution("hello", 3));       // "hhheeellllllooo"
    }
}
