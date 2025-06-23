// Heap 클래스 정의 (Min-Heap)
class Heap {
    // 힙 데이터 저장 배열
    #heap = [];

    // 값 추가
    push(value) {
        this.#heap.push(value);
        this.#bubbleUp();
    }

    // 최상위 요소 제거 및 반환
    pop() {
        if (this.#heap.length === 0) return null;
        if (this.#heap.length === 1) return this.#heap.pop();

        const top = this.#heap[0];
        this.#heap[0] = this.#heap.pop();
        this.#sinkDown();
        return top;
    }

    // 최상위 요소 반환 (삭제 안 함)
    peek() {
        return this.#heap[0] ?? null;
    }

    // 현재 힙 크기 반환
    size() {
        return this.#heap.length;
    }

    // 내부 메서드: 위로 올리기
    #bubbleUp() {
        let index = this.#heap.length - 1;
        const value = this.#heap[index];

        while (index > 0) {
            const parentIndex = Math.floor((index - 1) / 2);
            const parent = this.#heap[parentIndex];

            if (value[0] >= parent[0]) break;

            this.#heap[index] = parent;
            this.#heap[parentIndex] = value;
            index = parentIndex;
        }
    }

    // 내부 메서드: 아래로 내리기
    #sinkDown() {
        let index = 0;
        const length = this.#heap.length;
        const value = this.#heap[0];

        while (true) {
            const leftIndex = 2 * index + 1;
            const rightIndex = 2 * index + 2;
            let smallest = index;

            if (leftIndex < length && this.#heap[leftIndex][0] < this.#heap[smallest][0]) {
                smallest = leftIndex;
            }

            if (rightIndex < length && this.#heap[rightIndex][0] < this.#heap[smallest][0]) {
                smallest = rightIndex;
            }

            if (smallest === index) break;

            this.#heap[index] = this.#heap[smallest];
            this.#heap[smallest] = value;
            index = smallest;
        }
    }
}

// 디스크 컨트롤러 문제 해결 함수
function solution(jobs) {
    // 총 반환 시간 누적 변수
    let answer = 0;

    // 현재 시간
    let now = 0;

    // 처리된 작업 수
    let i = 0;

    // 마지막 작업 시작 시각
    let start = -1;

    // 최소 힙 생성
    const heap = new Heap();

    // 모든 작업을 처리할 때까지 반복
    while (i < jobs.length) {
        // 현재 시간까지 요청된 작업을 힙에 추가
        for (let job of jobs) {
            const [request, duration] = job;

            if (start < request && request <= now) {
                // (소요 시간, 요청 시간) 형식으로 저장
                heap.push([duration, request]);
            }
        }

        // 힙에 처리할 작업이 있는 경우
        if (heap.size() > 0) {
            // 소요 시간이 가장 짧은 작업 꺼내기
            const [duration, request] = heap.pop();

            // 작업 시작 시간 업데이트
            start = now;

            // 현재 시간 증가
            now += duration;

            // 반환 시간 누적
            answer += now - request;

            // 처리된 작업 수 증가
            i += 1;

        } else {
            // 대기 작업이 없으면 현재 시간 1 증가
            now += 1;
        }
    }

    // 평균 반환 시간의 정수 부분 반환
    return Math.floor(answer / jobs.length);
}

// 테스트 실행
console.log(solution([[0, 3], [1, 9], [3, 5]])); // 8