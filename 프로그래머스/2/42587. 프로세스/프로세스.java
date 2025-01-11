import java.util.*;

public class Solution {
    public int solution(int[] priorities, int location) {
        // 우선순위 큐 생성 (우선순위가 높은 순으로 관리)
        PriorityQueue<Integer> priorityQueue = new PriorityQueue<>(Collections.reverseOrder());
        Queue<int[]> queue = new LinkedList<>();

        // 초기 큐와 우선순위 큐 채우기
        for (int i = 0; i < priorities.length; i++) {
            queue.add(new int[]{i, priorities[i]});
            priorityQueue.add(priorities[i]);
        }

        int executedCount = 0;

        // 큐가 빌 때까지 반복 -> O(n)
        // 최종 시간 복잡도 -> O(nlogn)
        while (!queue.isEmpty()) {
            int[] current = queue.poll(); // 큐에서 첫 번째 프로세스를 가져옴 -> O(1)

            // 현재 프로세스가 최고 우선순위인지 확인
            if (current[1] < priorityQueue.peek()) {
                queue.add(current); // 우선순위가 높지 않으면 뒤로 보냄 -> O(1)
            } else {
                // 최고 우선순위인 경우 실행
                priorityQueue.poll(); // 실행한 우선순위를 우선순위 큐에서 제거 -> O(logn)
                executedCount++;

                // 실행한 프로세스가 원하는 위치의 프로세스라면 반환
                if (current[0] == location) {
                    return executedCount;
                }
            }
        }

        return -1; // 실제로 도달하지 않음
    }

    public static void main(String[] args) {
        Solution solution = new Solution();

        int[] priorities1 = {2, 1, 3, 2};
        int location1 = 2;
        System.out.println(solution.solution(priorities1, location1)); // 1

        int[] priorities2 = {1, 1, 9, 1, 1, 1};
        int location2 = 0;
        System.out.println(solution.solution(priorities2, location2)); // 5
    }
}
