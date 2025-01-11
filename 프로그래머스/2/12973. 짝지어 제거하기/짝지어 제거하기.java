import java.util.Deque;
import java.util.ArrayDeque;

public class Solution {
    public int solution(String s) {
        // 문자를 저장할 deque 초기화
        Deque<Character> stack = new ArrayDeque<>();

        // 문자열의 각 문자를 순회
        for (char charAt : s.toCharArray()) {
            // deque가 비어 있지 않고, deque의 최상단 문자와 현재 문자가 같으면
            if (!stack.isEmpty() && stack.peekLast() == charAt) {
                // deque의 최상단 문자를 제거
                stack.pollLast();
            } else {
                // 그렇지 않으면 현재 문자를 deque에 추가
                stack.addLast(charAt);
            }
        }

        // deque가 비어 있으면 모든 문자를 짝지어 제거할 수 있었음을 의미하므로 1
        // deque가 비어 있지 않으면 짝지어 제거할 수 없는 문자가 남아 있음을 의미하므로 0
        return stack.isEmpty() ? 1 : 0;
    }

    public static void main(String[] args) {
        Solution sol = new Solution();
        String s = "baabaa"; // 테스트 값
        System.out.println(sol.solution(s)); // 결과 출력
    }
}