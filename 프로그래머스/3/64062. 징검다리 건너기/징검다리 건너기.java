/**
 * 프로그래머스 64062 - 징검다리 건너기
 * https://school.programmers.co.kr/learn/courses/30/lessons/64062
 */
import java.util.Deque;
import java.util.LinkedList;

public class Solution {
    public int solution(int[] stones, int k) {
        int answer = Integer.MAX_VALUE; // 결과를 저장할 변수, 초기값은 무한대
        Deque<Integer> deque = new LinkedList<>(); // 윈도우 내 최대값을 관리할 deque

        for (int idx = 0; idx < stones.length; idx++) {
            int stone = stones[idx];

            // 현재 징검다리의 값이 deque의 마지막 요소보다 크면, deque의 마지막 요소 제거
            while (!deque.isEmpty() && stones[deque.getLast()] < stone) {
                deque.removeLast();
            }

            deque.addLast(idx); // 현재 징검다리의 인덱스를 deque에 추가

            // 윈도우의 범위를 벗어난 인덱스 제거
            if (deque.getFirst() == idx - k) {
                deque.removeFirst();
            }

            // 현재 idx까지의 최대값들 중 최소값 갱신
            if (idx >= k - 1) {
                answer = Math.min(answer, stones[deque.getFirst()]);
            }
        }

        return answer;
    }

    public static void main(String[] args) {
        Solution sol = new Solution();
        System.out.println(sol.solution(new int[]{2, 4, 5, 3, 2, 1, 4, 2, 5, 1}, 3)); // 3
    }
}
