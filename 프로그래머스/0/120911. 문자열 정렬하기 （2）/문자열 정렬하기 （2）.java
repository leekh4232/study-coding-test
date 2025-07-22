import java.util.Arrays;

public class Solution {

    public static String solution(String my_string) {
        // 1. 문자열을 소문자로 변환
        String lower = my_string.toLowerCase();

        // 2. 문자 배열로 변환 후 정렬
        char[] chars = lower.toCharArray();
        Arrays.sort(chars);  // 알파벳 순서대로 정렬

        // 3. 정렬된 문자 배열을 문자열로 변환
        return new String(chars);
    }

    // ✅ 테스트 실행
    public static void main(String[] args) {
        System.out.println(solution("Bcad"));    // abcd
        System.out.println(solution("heLLo"));   // ehllo
        System.out.println(solution("Python"));  // hnopty
    }
}
