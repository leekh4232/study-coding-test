import java.util.*;

public class Solution {

    // 짝지어 제거하기를 성공적으로 수행할 수 있는지 확인하는 메서드
    public static int solution(String s) {
        // 문자 제거를 위한 스택 초기화
        Deque<Character> stack = new ArrayDeque<>();

        // 문자열을 순회하며 문자 제거 처리
        for (char ch : s.toCharArray()) {
            // 스택이 비어있지 않고, 최상단 문자와 현재 문자가 같으면 제거
            if (!stack.isEmpty() && stack.peek() == ch) {
                stack.pop();
            } 
            // 그렇지 않으면 스택에 추가
            else {
                stack.push(ch);
            }
        }

        // 스택이 비어 있으면 모든 문자가 제거된 것이므로 1, 아니면 0 반환
        return stack.isEmpty() ? 1 : 0;
    }

    public static void main(String[] args) {
        // ✅ 예제 테스트 실행
        System.out.println(solution("baabaa")); // 결과: 1
        System.out.println(solution("cdcd"));   // 결과: 0
    }
}
