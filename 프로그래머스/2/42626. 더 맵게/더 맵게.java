import java.util.PriorityQueue;

public class Solution {

    // 최소 횟수로 모든 음식의 스코빌 지수를 K 이상으로 만드는 메서드
    public static int solution(int[] scoville, int K) {
        // 최소 힙(Min-Heap)을 구현하기 위한 우선순위 큐 선언
        PriorityQueue<Integer> heap = new PriorityQueue<>();

        // 모든 스코빌 지수를 힙에 삽입
        for (int s : scoville) {
            heap.offer(s);
        }

        // 섞은 횟수를 저장할 변수
        int cnt = 0;

        // 힙의 최소값이 K 이상이 될 때까지 반복
        while (heap.peek() < K) {
            // 음식이 하나만 남은 경우 더 이상 섞을 수 없음
            if (heap.size() == 1) {
                return -1;
            }

            // 가장 맵지 않은 음식 꺼냄
            int first = heap.poll();

            // 두 번째로 맵지 않은 음식 꺼냄
            int second = heap.poll();

            // 새 음식의 스코빌 지수 계산
            int newFood = first + (second * 2);

            // 새 음식을 힙에 삽입
            heap.offer(newFood);

            // 섞은 횟수 증가
            cnt++;
        }

        // 모든 음식이 K 이상일 때 섞은 횟수 반환
        return cnt;
    }

    // 테스트 케이스 실행을 위한 main 메서드
    public static void main(String[] args) {
        int[] scoville = {1, 2, 3, 9, 10, 12};
        int K = 7;

        // 결과 출력
        System.out.println(solution(scoville, K)); // 출력: 2
    }
}
