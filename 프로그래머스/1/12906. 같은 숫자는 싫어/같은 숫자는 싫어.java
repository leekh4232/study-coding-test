import java.util.*;

public class Solution {

    // Stack을 사용하여 연속적으로 중복된 숫자를 제거하는 메서드
    public static int[] solution(int[] arr) {
        // 결과를 저장할 스택
        Stack<Integer> stack = new Stack<>();

        // 배열을 순회하면서 연속된 숫자를 제거
        for (int num : arr) {
            // 스택이 비어있거나, 이전 숫자와 다를 때만 추가
            if (stack.isEmpty() || stack.peek() != num) {
                stack.push(num);
            }
        }

        // 스택의 데이터를 배열로 변환하여 반환
        int[] result = new int[stack.size()];
        for (int i = 0; i < result.length; i++) {
            result[i] = stack.get(i);
        }
        return result;
    }

    public static void main(String[] args) {
        // ✅ 예제 테스트 실행
        System.out.println(Arrays.toString(solution(new int[]{1, 1, 3, 3, 0, 1, 1})));
        System.out.println(Arrays.toString(solution(new int[]{4, 4, 4, 3, 3})));
    }
}