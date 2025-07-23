import java.util.*;

public class Solution {

    public static String solution(String s) {
        List<Character> once = new ArrayList<>();

        while (!s.isEmpty()) {
            char a = s.charAt(0);         // 첫 번째 문자
            String b = s.substring(1);    // 나머지 문자열

            if (b.indexOf(a) == -1) {
                once.add(a);              // b에 a가 없으면 한 번만 등장 → 저장
            } else {
                b = b.replace(String.valueOf(a), "");  // a를 b에서 제거
            }

            s = b; // 다음 반복을 위해 s 업데이트
        }

        // 리스트를 문자열로 변환
        Collections.sort(once);
        StringBuilder result = new StringBuilder();
        for (char c : once) {
            result.append(c);
        }

        return result.toString();
    }

    // ✅ 테스트 실행
    public static void main(String[] args) {
        System.out.println(solution("abcabcadc")); // "d"
        System.out.println(solution("abdc"));      // "abcd"
        System.out.println(solution("hello"));     // "eho"
    }
}
