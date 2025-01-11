import java.util.*;

public class Solution {
    public Deque<Integer> solution(int []arr) {
        // 정수 배열 arr을 입력으로 받아, 결과를 저장할 스택
        Deque<Integer> answer = new ArrayDeque<>();
        // 이전 숫자를 저장할 변수 previous를 -1로 초기화
        // --> 첫 번째 숫자와 비교할 때 사용
        int previous = -1;

        // 배열 arr의 각 요소를 순회
        for (int num : arr) {
            // 현재 숫자가 이전 숫자와 다를 경우
            if (num != previous) {
                // answer 리스트에 현재 숫자를 추가
                answer.add(num);
                // 이전 숫자를 현재 숫자로 업데이트
                // --> 연속으로 나타나는 같은 숫자는 리스트에 추가되지 않게 됨.
                previous = num;
            }
        }

        return answer;
    }
}