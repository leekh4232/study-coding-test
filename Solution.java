import java.util.*;

public class Solution {
    public static int solution(int[] A, int K) {
        // Java의 Min-Heap (PriorityQueue는 기본이 최소 힙)
        PriorityQueue<Integer> minHeap = new PriorityQueue<>();

        // 배열 A의 모든 요소를 힙에 추가 (heapify와 동일)
        for (int num : A) {
            minHeap.offer(num);
        }

        // 가장 작은 값을 K-1번 제거
        for (int i = 0; i < K - 1; i++) {
            minHeap.poll();
        }

        // K번째로 작은 값 반환
        return minHeap.poll();
    }

    public static void main(String[] args) {
        int[] A = {4, 1, 2, 3, 5};
        int K = 2;

        int result = solution(A, K);
        System.out.println(result); // 출력: 2
    }
}
