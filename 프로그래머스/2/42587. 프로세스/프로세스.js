class PriorityQueue {
    #heap = [];

    // 요소 삽입: [priority, value]
    put([priority, value]) {
        this.#heap.push([priority, value]);
        this.#bubbleUp();
    }

    // 최상단 요소 제거 및 반환
    get() {
        if (this.#heap.length <= 1) return this.#heap.pop();
        const min = this.#heap[0];
        this.#heap[0] = this.#heap.pop();
        this.#sinkDown();
        return min;
    }

    // 최상단 요소 확인
    peek() {
        return this.#heap[0];
    }

    // 큐가 비었는지 확인
    isEmpty() {
        return this.#heap.length === 0;
    }

    // 큐 크기 반환
    size() {
        return this.#heap.length;
    }

    // 삽입 후 위로 올리는 동작
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

    // 제거 후 아래로 내리는 동작
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

// 프로세스 실행 순서를 구하는 함수
function solution(priorities, location) {
    // 우선순위 큐 생성
    const priorityQueue = new PriorityQueue();

    // 모든 우선순위를 음수로 변환해서 삽입
    for (let priority of priorities) {
        priorityQueue.put([-priority, null]); // 값은 사용하지 않으므로 null
    }

    // 대기 큐 초기화 (인덱스와 함께 저장)
    const queue = priorities.map((priority, index) => [index, priority]);

    // 실행 순서 카운트
    let executedCount = 0;

    // 큐가 빌 때까지 반복
    while (queue.length > 0) {
        // 앞에서 요소를 꺼냄
        const [currentIdx, currentPriority] = queue.shift();

        // 현재 우선순위가 최고인지 확인
        const [topPriority] = priorityQueue.peek();

        if (currentPriority < -topPriority) {
            // 최고 우선순위가 아니면 큐 뒤로 이동
            queue.push([currentIdx, currentPriority]);
        } else {
            // 최고 우선순위면 실행
            priorityQueue.get();
            executedCount++;

            // 실행된 프로세스가 목표 위치이면 결과 반환
            if (currentIdx === location) {
                return executedCount;
            }
        }
    }
}

// 테스트 케이스 실행
console.log(solution([2, 1, 3, 2], 2)); // 1
console.log(solution([1, 1, 9, 1, 1, 1], 0)); // 5