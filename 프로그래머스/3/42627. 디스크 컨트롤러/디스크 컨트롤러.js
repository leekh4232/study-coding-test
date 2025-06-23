// 최소 힙을 구현하는 클래스
class MinHeap {
    // 힙을 저장할 배열 초기화
    constructor() {
        this.heap = [];
    }

    // 요소를 힙에 삽입
    push(value) {
        // 배열 끝에 추가
        this.heap.push(value);
        // 위로 올리며 정렬 유지
        this.bubbleUp();
    }

    // 가장 작은 요소를 꺼냄
    pop() {
        // 힙이 비어 있으면 undefined 반환
        if (this.heap.length === 0) return undefined;

        // 최솟값 저장
        const min = this.heap[0];

        // 마지막 요소를 꺼내 루트에 배치
        const end = this.heap.pop();

        // 요소가 남아 있다면 재정렬
        if (this.heap.length > 0) {
            this.heap[0] = end;
            this.sinkDown();
        }

        // 꺼낸 최솟값 반환
        return min;
    }

    // 힙 크기 반환
    size() {
        return this.heap.length;
    }

    // 삽입된 요소를 위로 올리며 힙 구조 유지
    bubbleUp() {
        let idx = this.heap.length - 1;
        const element = this.heap[idx];

        while (idx > 0) {
            let parentIdx = Math.floor((idx - 1) / 2);
            let parent = this.heap[parentIdx];

            // 소요 시간이 작을수록 우선순위 높음
            if (element[0] >= parent[0]) break;

            // 부모와 교환
            this.heap[parentIdx] = element;
            this.heap[idx] = parent;
            idx = parentIdx;
        }
    }

    // 루트 요소를 아래로 내리며 힙 구조 유지
    sinkDown() {
        let idx = 0;
        const length = this.heap.length;
        const element = this.heap[0];

        while (true) {
            let leftIdx = 2 * idx + 1;
            let rightIdx = 2 * idx + 2;
            let left, right;
            let swap = null;

            if (leftIdx < length) {
                left = this.heap[leftIdx];
                if (left[0] < element[0]) {
                    swap = leftIdx;
                }
            }

            if (rightIdx < length) {
                right = this.heap[rightIdx];
                if (
                    (swap === null && right[0] < element[0]) ||
                    (swap !== null && right[0] < left[0])
                ) {
                    swap = rightIdx;
                }
            }

            if (swap === null) break;

            this.heap[idx] = this.heap[swap];
            this.heap[swap] = element;
            idx = swap;
        }
    }
}

// 평균 반환 시간을 최소화하는 디스크 스케줄링 함수
function solution(jobs) {
    // 누적 반환 시간
    let answer = 0;

    // 현재 시간
    let now = 0;

    // 처리된 작업 수
    let i = 0;

    // 마지막 작업 시작 시각
    let start = -1;

    // 최소 힙 (작업 소요 시간 기준)
    const heap = new MinHeap();

    // 전체 작업이 처리될 때까지 반복
    while (i < jobs.length) {
        // 현재 시간까지 도착한 작업을 힙에 삽입
        for (let j = 0; j < jobs.length; j++) {
            const [request, duration] = jobs[j];

            if (start < request && request <= now) {
                // (작업 소요 시간, 요청 시각) 형식으로 삽입
                heap.push([duration, request]);
            }
        }

        // 처리할 작업이 있다면
        if (heap.size() > 0) {
            // 가장 소요 시간이 짧은 작업 꺼냄
            const [duration, request] = heap.pop();

            // 작업 시작 시각 업데이트
            start = now;

            // 작업 소요 시간만큼 현재 시간 증가
            now += duration;

            // 반환 시간 누적: 종료 시간 - 요청 시간
            answer += now - request;

            // 작업 처리 수 증가
            i++;
        } else {
            // 대기 중인 작업이 없다면 시간 1 증가
            now++;
        }
    }

    // 평균 반환 시간의 정수 부분 반환
    return Math.floor(answer / jobs.length);
}

// 테스트 케이스 실행
console.log(solution([[0, 3], [1, 9], [3, 5]]));  // 8
