import java.util.Arrays;
import java.util.Collections;
import java.util.PriorityQueue;

public class Main {
    public static void main(String[] args) {
        // 초기 배열
        Integer[] data = {5, 1, 3, 2, 8, 7};

        // PriorityQueue를 사용해 자동으로 힙 구조 생성 (Min-Heap)
        PriorityQueue<Integer> heap = new PriorityQueue<>(Collections.reverseOrder());
        heap.addAll(Arrays.asList(data));

        // 힙 요소 출력
        System.out.print("Heapified: ");
        while (!heap.isEmpty()) {
            System.out.print(heap.poll() + " ");
        }
    }
}