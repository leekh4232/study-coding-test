import java.util.*;

public class Solution {

    public static String[] solution(String my_str, int n) {
        List<String> result = new ArrayList<>();

        int length = my_str.length();
        for (int i = 0; i < length; i += n) {
            // i부터 n글자 잘라내되, 범위를 초과하면 끝까지
            int end = Math.min(i + n, length);
            result.add(my_str.substring(i, end));
        }

        // List<String> → String[]
        return result.toArray(new String[0]);
    }

    // ✅ 테스트 실행
    public static void main(String[] args) {
        System.out.println(Arrays.toString(solution("abc1Addfggg4556b", 6)));
        // 출력: [abc1Ad, dfggg4, 556b]

        System.out.println(Arrays.toString(solution("abcdef123", 3)));
        // 출력: [abc, def, 123]
    }
}
