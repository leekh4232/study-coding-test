import java.util.*;

public class Solution {

    // 올바른 괄호 문자열인지 판별하는 메서드
    public static boolean solution(String s) {
        // 스택을 사용하여 괄호를 관리
        Deque<Character> stack = new ArrayDeque<>();

        // 문자열을 순회하며 검사
        for (char ch : s.toCharArray()) {
            // 여는 괄호 '('는 스택에 추가
            if (ch == '(') {
                stack.push(ch);
            } 
            // 닫는 괄호 ')'가 나오면 처리
            else {
                // 스택이 비어 있으면 올바르지 않은 괄호
                if (stack.isEmpty()) {
                    return false;
                }
                // 스택에서 '(' 제거
                stack.pop();
            }
        }

        // 스택이 비어 있으면 올바른 괄호, 그렇지 않으면 잘못된 괄호
        return stack.isEmpty();
    }

    public static void main(String[] args) {
        // ✅ 예제 테스트 실행
        System.out.println(solution("()()"));     // true
        System.out.println(solution("(())()"));   // true
        System.out.println(solution(")()("));     // false
        System.out.println(solution("(()("));     // false
        System.out.println(solution("()"));       // true
        System.out.println(solution(")("));       // false
        System.out.println(solution(")"));        // false
        System.out.println(solution("("));        // false
        System.out.println(solution("))"));       // false
        System.out.println(solution("(("));       // false
    }
}
