import java.util.*;

public class Solution {

    public static String solution(String rsp) {
        // 1. 이기는 규칙을 Map으로 정의
        Map<Character, Character> winMap = new HashMap<>();
        winMap.put('0', '5');  // 바위(0)는 보(5)를 이김
        winMap.put('2', '0');  // 가위(2)는 바위(0)를 이김
        winMap.put('5', '2');  // 보는 가위(2)에게 짐 → 가위가 이김

        // 2. 결과를 저장할 StringBuilder
        StringBuilder result = new StringBuilder();

        // 3. 각 문자에 대해 변환
        for (int i = 0; i < rsp.length(); i++) {
            char c = rsp.charAt(i);
            result.append(winMap.get(c));
        }

        // 4. 결과 문자열 반환
        return result.toString();
    }

    // ✅ 테스트 실행
    public static void main(String[] args) {
        System.out.println(solution("2"));     // 출력: 0
        System.out.println(solution("205"));   // 출력: 052
    }
}
