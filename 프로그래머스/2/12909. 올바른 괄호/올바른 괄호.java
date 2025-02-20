/**
 * 프로그래머스 12909번 - 올바른_괄호
 * https://school.programmers.co.kr/learn/courses/30/lessons/12909
 */
import java.util.ArrayDeque;
import java.util.Deque;

public class Solution {
    // 문자열 s가 올바른 괄호 문자열인지 확인하는 함수
    // --> Stack 자료구조를 사용하여 여는 괄호와 닫는 괄호의 짝을 맞춤
    public boolean solution(String s) {
        // 빈 스택을 생성 --> 여는 괄호를 저장하는 용도
        Deque<Character> deque = new ArrayDeque<>();

        // 문자열 s의 각 글자를 순회
        for (char ch : s.toCharArray()) {
            if (ch == '(') {            // 여는 괄호인 경우
                deque.push(ch);          // 스택에 추가
            } else if (ch == ')') {     // 닫는 괄호인 경우
                if (deque.isEmpty()) {  // 스택이 비어 있으면 false
                    return false;
                }
                deque.pop(); // 스택에서 여는 괄호를 팝(pop)하여 짝을 맞춤
            }
        }

        // 문자열 s의 모든 문자를 순회한 후, 스택이 비어 있는지 확인
        // --> 올바른 괄호 문자열이라면 최종적으로는 스택이 비어 있어야 함
        return deque.isEmpty();
    }

    public static void main(String[] args) {
        Solution ex = new Solution();

        // 테스트 케이스 1 -> true
        System.out.println(ex.solution("()()"));

        // 테스트 케이스 2 -> true
        System.out.println(ex.solution("(())()"));

        // 테스트 케이스 3 -> false
        System.out.println(ex.solution(")()("));

        // 테스트 케이스 4 -> false
        System.out.println(ex.solution("(()("));
    }
}