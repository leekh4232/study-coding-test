import java.util.*;

public class Solution {

    // 특정 프로세스가 몇 번째로 실행되는지 계산하는 메서드
    public static int solution(int[] priorities, int location) {
        // 우선순위 큐(최대 힙)를 생성하여 가장 높은 우선순위 추적
        PriorityQueue<Integer> priorityQueue = new PriorityQueue<>(Collections.reverseOrder());

        // 프로세스 우선순위를 우선순위 큐에 저장
        for (int priority : priorities) {
            priorityQueue.add(priority);
        }

        // (인덱스, 우선순위) 형태로 저장하는 일반 큐
        Queue<int[]> queue = new LinkedList<>();
        for (int i = 0; i < priorities.length; i++) {
            queue.add(new int[]{i, priorities[i]});
        }

        int executedCount = 0; // 실행된 프로세스 개수

        while (!queue.isEmpty()) {
            // 큐에서 맨 앞의 프로세스를 가져옴
            int[] currentProcess = queue.poll();
            int currentIndex = currentProcess[0];
            int currentPriority = currentProcess[1];

            // 현재 프로세스가 가장 높은 우선순위인지 확인
            if (currentPriority < priorityQueue.peek()) {
                // 최고 우선순위가 아니라면 다시 큐의 뒤로 이동
                queue.add(currentProcess);
            } else {
                // 실행된 프로세스를 우선순위 큐에서 제거
                priorityQueue.poll();
                executedCount++; // 실행된 프로세스 개수 증가

                // 실행된 프로세스가 찾는 프로세스라면 실행 순서 반환
                if (currentIndex == location) {
                    return executedCount;
                }
            }
        }

        return -1; // 이론적으로 실행되지 않는 경우는 없음
    }

    public static void main(String[] args) {
        // ✅ 예제 테스트 실행
        System.out.println(solution(new int[]{2, 1, 3, 2}, 2)); // 결과: 1
        System.out.println(solution(new int[]{1, 1, 9, 1, 1, 1}, 0)); // 결과: 5
    }
}
