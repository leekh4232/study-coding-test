class PriorityQueue {
    #heap = [];

    // 요소 삽입: [priority, value]
    put([priority, value]) {
        this.#heap.push([priority, value]);
        this.#bubbleUp();
    }

    // 요소 제거: 우선순위 가장 높은 요소 반환
    get() {
        if (this.#heap.length <= 1) return this.#heap.pop();
        const min = this.#heap[0];
        this.#heap[0] = this.#heap.pop();
        this.#sinkDown();
        return min;
    }

    // 최상단 요소 확인 (제거하지 않음)
    peek() {
        return this.#heap[0];
    }

    // 큐가 비었는지 여부 반환
    isEmpty() {
        return this.#heap.length === 0;
    }

    // 큐 크기 반환
    size() {
        return this.#heap.length;
    }

    // 요소가 삽입된 후 위로 올림
    #bubbleUp() {
        let index = this.#heap.length - 1;
        const element = this.#heap[index];

        while (index > 0) {
            const parentIndex = Math.floor((index - 1) / 2);
            const parent = this.#heap[parentIndex];

            if (element[0] > parent[0]) break;
            this.#heap[index] = parent;
            this.#heap[parentIndex] = element;
            index = parentIndex;
        }
    }

    // 요소가 제거된 후 아래로 내림
    #sinkDown() {
        let index = 0;
        const length = this.#heap.length;
        const element = this.#heap[0];

        while (true) {
            let left = 2 * index + 1;
            let right = 2 * index + 2;
            let smallest = index;

            if (left < length && this.#heap[left][0] < this.#heap[smallest][0]) smallest = left;
            if (right < length && this.#heap[right][0] < this.#heap[smallest][0]) smallest = right;

            if (smallest === index) break;
            [this.#heap[index], this.#heap[smallest]] = [this.#heap[smallest], this.#heap[index]];
            index = smallest;
        }
    }
}

// 이중 우선순위 큐를 구현하는 함수 (PriorityQueue 사용)
function solution(operations) {
    // 최소 힙: 값 그대로 저장
    const minHeap = new PriorityQueue();
    // 최대 힙처럼 사용: 우선순위를 음수로 저장
    const maxHeap = new PriorityQueue();

    // 주어진 연산 순회
    for (let op of operations) {
        const [cmd, valStr] = op.split(" ");
        const num = parseInt(valStr);

        if (cmd === "I") {
            // 삽입: 두 힙에 모두 값과 우선순위 함께 저장
            minHeap.put([num, num]);
            maxHeap.put([-num, num]);

        } else if (cmd === "D") {
            // 삭제 연산, 큐가 비었으면 무시
            if (minHeap.isEmpty()) continue;

            if (num === -1) {
                // 최소값 삭제: minHeap에서 꺼냄
                const [, minVal] = minHeap.get();

                // maxHeap에서 동일한 값을 직접 찾아 제거
                const buffer = [];
                while (!maxHeap.isEmpty()) {
                    const entry = maxHeap.get();
                    if (entry[1] === minVal) break;
                    buffer.push(entry);
                }
                // 제거 후 남은 항목 복원
                for (let item of buffer) maxHeap.put(item);

            } else {
                // 최대값 삭제: maxHeap에서 꺼냄
                const [, maxVal] = maxHeap.get();

                // minHeap에서 동일한 값을 직접 찾아 제거
                const buffer = [];
                while (!minHeap.isEmpty()) {
                    const entry = minHeap.get();
                    if (entry[1] === maxVal) break;
                    buffer.push(entry);
                }
                // 제거 후 남은 항목 복원
                for (let item of buffer) minHeap.put(item);
            }
        }
    }

    // 최종 결과 반환
    if (minHeap.isEmpty()) {
        return [0, 0];
    } else {
        const [, minVal] = minHeap.peek();
        const [, maxVal] = maxHeap.peek();
        return [maxVal, minVal];
    }
}

// 테스트 케이스 실행 (PriorityQueue 클래스 필요)
console.log(solution(["I 16", "I -5643", "D -1", "D 1", "D 1", "I 123", "D -1"])); // [0, 0]
console.log(solution(["I -45", "I 653", "D 1", "I -642", "I 45", "I 97", "D 1", "D -1", "I 333"])); // [333, -45]