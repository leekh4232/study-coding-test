import java.util.HashMap;
import java.util.Map;

public class Solution {

    public static String solution(String letter) {
        // 모스 부호 맵 초기화
        Map<String, String> morse = new HashMap<>();
        morse.put(".-", "a");   morse.put("-...", "b"); morse.put("-.-.", "c");
        morse.put("-..", "d");  morse.put(".", "e");    morse.put("..-.", "f");
        morse.put("--.", "g");  morse.put("....", "h"); morse.put("..", "i");
        morse.put(".---", "j"); morse.put("-.-", "k");  morse.put(".-..", "l");
        morse.put("--", "m");   morse.put("-.", "n");   morse.put("---", "o");
        morse.put(".--.", "p"); morse.put("--.-", "q"); morse.put(".-.", "r");
        morse.put("...", "s");  morse.put("-", "t");    morse.put("..-", "u");
        morse.put("...-", "v"); morse.put(".--", "w");  morse.put("-..-", "x");
        morse.put("-.--", "y"); morse.put("--..", "z");

        // 공백 기준으로 분할
        String[] parts = letter.split(" ");
        StringBuilder result = new StringBuilder();

        // 변환 처리
        for (String part : parts) {
            result.append(morse.get(part));
        }

        return result.toString();
    }

    // ✅ 테스트용 main 함수
    public static void main(String[] args) {
        System.out.println(solution(".... . .-.. .-.. ---"));     // hello
        System.out.println(solution(".--. -.-- - .... --- -."));  // python
    }
}
