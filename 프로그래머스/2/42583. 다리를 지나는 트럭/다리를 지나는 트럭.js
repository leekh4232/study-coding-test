// 트럭 여러 대가 무게 제한이 있는 다리를 순서대로 건너는 데 걸리는 최소 시간을 구하는 함수
function solution(bridgeLength, weight, truckWeights) {
    // 시간 경과를 추적하는 변수
    let time = 0;

    // 다리 위 상태를 표현하는 배열 (초기에는 모두 비어 있음 = 0)
    let bridge = Array(bridgeLength).fill(0);

    // 트럭 대기열을 복사하여 사용
    truckWeights = [...truckWeights];

    // 현재 다리 위에 있는 트럭들의 총 무게
    let currentWeight = 0;

    // 대기 트럭이 모두 건넜고, 다리 위에도 트럭이 없을 때까지 반복
    while (truckWeights.length > 0 || currentWeight > 0) {
        // 시간 1초 경과
        time++;

        // 다리에서 가장 먼저 들어온 트럭을 꺼냄
        const exitingTruck = bridge.shift();

        // 트럭이 빠졌다면 그 무게만큼 현재 무게에서 제거
        currentWeight -= exitingTruck;

        // 대기 중인 트럭이 있다면 다음 트럭을 다리에 올릴 수 있는지 확인
        if (truckWeights.length > 0) {
            // 다음 트럭의 무게를 더해도 무게 제한을 넘지 않으면
            if (currentWeight + truckWeights[0] <= weight) {
                // 트럭을 다리에 올림
                const newTruck = truckWeights.shift();

                // 다리에 트럭을 추가
                bridge.push(newTruck);

                // 다리 위 총 무게 갱신
                currentWeight += newTruck;
            } else {
                // 트럭을 못 올리면 빈 공간 유지 (0 추가)
                bridge.push(0);
            }
        } else {
            // 대기 트럭이 없더라도 다리는 계속 이동 → 0 추가
            bridge.push(0);
        }
    }

    // 모든 트럭이 다리를 건넌 총 시간 반환
    return time;
}

// ✅ 테스트 예제 실행
console.log(solution(2, 10, [7, 4, 5, 6]));  // 8
console.log(solution(100, 100, [10]));       // 101
console.log(solution(100, 100, [10,10,10,10,10,10,10,10,10,10]));  // 110
