/**
 * 프로그래머스 12906번 - 같은 숫자는 싫어
 * https://school.programmers.co.kr/learn/courses/30/lessons/12906
 */
import java.util.*;

public class Solution {
    // 주어진 배열에서 연속으로 나타나는 같은 숫자를 제거하고, 남은 숫자들을 순서대로 리스트에 담아 반환하는 함수
    public int[] solution(int []arr) {
        // 정수 배열 arr을 입력으로 받아, 결과를 저장할 스택
        Stack<Integer> mystack = new Stack<>();
        // 이전 숫자를 저장할 변수 previous를 -1로 초기화
        // --> 첫 번째 숫자와 비교할 때 사용
        int previous = -1;

        // 배열 arr의 각 요소를 순회
        for (int num : arr) {
            // 현재 숫자가 이전 숫자와 다를 경우
            if (num != previous) {
                // answer 리스트에 현재 숫자를 추가
                mystack.push(num);
                // 이전 숫자를 현재 숫자로 업데이트
                // --> 연속으로 나타나는 같은 숫자는 리스트에 추가되지 않게 됨.
                previous = num;
            }
        }

        int[] answer = new int[mystack.size()];

        // 스택에 있는 요소를 배열에 담기
        for (int i = mystack.size() - 1; i >= 0; i--) {
            answer[i] = mystack.pop();
        }

        return answer;
    }

    public static void main(String[] args) {
        Solution ex = new Solution();

        // 첫 번째 테스트 케이스 실행 -> [1, 3, 0, 1]
        System.out.println(Arrays.toString(ex.solution(new int[]{1, 1, 3, 3, 0, 1, 1})));

        // 두 번째 테스트 케이스 실행 -> [4, 3]
        System.out.println(Arrays.toString(ex.solution(new int[]{4, 4, 4, 3, 3})));
    }
}