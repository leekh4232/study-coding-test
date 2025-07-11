import java.util.*;

public class Solution {

    // 모든 트럭이 다리를 건너는 최소 시간을 계산하는 메서드
    public static int solution(int bridgeLength, int weight, int[] truckWeights) {
        int time = 0; // 경과 시간
        int currentWeight = 0; // 현재 다리 위의 총 무게

        // 다리 위의 상태를 유지할 큐 (다리 길이만큼 0으로 초기화)
        Queue<Integer> bridge = new LinkedList<>();
        for (int i = 0; i < bridgeLength; i++) {
            bridge.add(0);
        }

        // 대기 중인 트럭을 저장할 큐
        Queue<Integer> waitingTrucks = new LinkedList<>();
        for (int truck : truckWeights) {
            waitingTrucks.add(truck);
        }

        while (!waitingTrucks.isEmpty() || currentWeight > 0) {
            time++; // 시간 증가

            // 다리에서 트럭 제거 (앞에서 나가는 트럭)
            int exitingTruck = bridge.poll();
            currentWeight -= exitingTruck; // 다리에서 빠진 트럭의 무게 감소

            // 새로운 트럭을 다리에 올릴 수 있는지 확인
            if (!waitingTrucks.isEmpty()) {
                if (currentWeight + waitingTrucks.peek() <= weight) {
                    // 새로운 트럭이 올라갈 수 있는 경우
                    int newTruck = waitingTrucks.poll();
                    bridge.add(newTruck);
                    currentWeight += newTruck; // 다리 무게 증가
                } else {
                    // 트럭이 올라갈 수 없으면 다리에 빈 공간 추가
                    bridge.add(0);
                }
            } else {
                // 더 이상 올릴 트럭이 없을 경우, 빈 공간 추가
                bridge.add(0);
            }
        }

        return time; // 모든 트럭이 다리를 건너는 데 걸린 총 시간 반환
    }

    public static void main(String[] args) {
        // ✅ 예제 테스트 실행
        System.out.println(solution(2, 10, new int[]{7, 4, 5, 6})); // 결과: 8
        System.out.println(solution(100, 100, new int[]{10})); // 결과: 101
        System.out.println(solution(100, 100, new int[]{10, 10, 10, 10, 10, 10, 10, 10, 10, 10})); // 결과: 110
    }
}
