import java.util.*;

public class Solution {

    // 주식 가격이 떨어지지 않은 기간을 계산하는 메서드
    public static int[] solution(int[] prices) {
        int n = prices.length; // 주식 가격 배열의 길이
        int[] answer = new int[n]; // 결과 배열 초기화

        // 가격이 떨어질 가능성이 있는 인덱스를 저장할 스택
        Deque<Integer> stack = new ArrayDeque<>();

        // 주식 가격 배열을 순회하며 가격이 떨어지는 순간을 찾음
        for (int i = 0; i < n; i++) {
            // 스택이 비어있지 않고, 현재 가격이 스택 최상단 가격보다 낮으면
            while (!stack.isEmpty() && prices[stack.peek()] > prices[i]) {
                int j = stack.pop(); // 스택에서 인덱스 꺼내기
                answer[j] = i - j; // 가격이 유지된 기간 계산
            }
            // 현재 인덱스를 스택에 추가
            stack.push(i);
        }

        // 스택에 남아있는 인덱스들은 끝까지 가격이 유지된 경우
        while (!stack.isEmpty()) {
            int j = stack.pop();
            answer[j] = n - 1 - j;
        }

        return answer;
    }

    public static void main(String[] args) {
        // ✅ 예제 테스트 실행
        System.out.println(Arrays.toString(solution(new int[]{1, 2, 3, 2, 3}))); // 결과: [4, 3, 1, 1, 0]
    }
}
