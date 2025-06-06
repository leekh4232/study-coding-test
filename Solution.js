class PriorityQueue {
    /** 내부 힙 배열 */
    #heap = [];

    /** 요소를 큐에 추가 - 우선순위와 값을 받아서 객체로 만든 뒤 힙에 추가하고 정렬 */
    push(priority, value) {
        this.#heap.push({ priority, value });   // 힙 배열 끝에 노드 추가 - {우선순위, 값}
        this.#bubbleUp();                       // 힙의 성질을 유지하도록 위로 올리기
    }

    /** 우선순위가 가장 높은(숫자가 가장 작은) 요소를 꺼냄 */
    pop() {
        if (this.size() === 0) return null;     // 힙이 비어있으면 null 반환
        const top = this.#heap[0];              // 최상단 노드를 저장
        const last = this.#heap.pop();          // 마지막 요소를 꺼내고

        if (this.size() !== 0) {                // 요소가 남아 있다면?
            this.#heap[0] = last;               // 마지막 요소를 맨 위로 올리고-
            this.#sinkDown();                   // 정렬
        }

        return top.value;                       // 최상단 노드 반환
    }

    /** 최상단 요소를 확인 (제거하지 않음) */
    peek() {
        return this.#heap[0].value || null;
    }

    /** 현재 큐의 크기 반환 */
    size() {
        return this.#heap.length;
    }

    /** 힙 정렬 - 마지막 요소를 올바른 위치로 올림 */
    #bubbleUp() {
        let index = this.#heap.length - 1;                  // 마지막 요소의 인덱스
        const node = this.#heap[index];                     // 이동할 노드

        // 부모 노드와 비교하면서 조건 만족하지 않으면 스왑
        while (index > 0) {
            const parentIdx = Math.floor((index - 1) / 2);  // 부모 노드의 인덱스 계산
            const parent = this.#heap[parentIdx];

            // 부모 우선순위가 현재 우선순위보다 작거나, 우선순위가 같지만 값이 작으면 멈춤
            if (parent.priority < node.priority ||
                (parent.priority === node.priority && parent.value <= node.value)) {
                    break;
            }

            this.#heap[index] = this.#heap[parentIdx];      // 부모를 아래로 이동
            index = parentIdx;
        }

        this.#heap[index] = node;                           // 현재 노드를 적절한 위치에 삽입
    }

    /** 힙 정렬 - 최상단 요소를 아래로 내림 */
    #sinkDown() {
        let index = 0;                          // 시작 인덱스
        const length = this.#heap.length;
        const node = this.#heap[0];

        while (true) {
            const leftIdx = 2 * index + 1;      // 왼쪽 자식 인덱스
            const rightIdx = 2 * index + 2;     // 오른쪽 자식 인덱스
            let smallest = index;               // 가장 작은 값을 가진 인덱스 추적

            // 왼쪽 자식이 작고, 왼쪽의 우선순위가 작거나 우선순위가 같지만 왼쪽의 값이 더 작으면 그 인덱스로 변경
            if (leftIdx < length && (
                    this.#heap[leftIdx].priority < this.#heap[smallest].priority || (
                            this.#heap[leftIdx].priority === this.#heap[smallest].priority &&
                            this.#heap[leftIdx].value < this.#heap[smallest].value))) {
                smallest = leftIdx;
            }

            // 오른쪽 자식도 비교
            if (rightIdx < length && (
                this.#heap[rightIdx].priority < this.#heap[smallest].priority || (
                    this.#heap[rightIdx].priority === this.#heap[smallest].priority &&
                    this.#heap[rightIdx].value < this.#heap[smallest].value))) {
                smallest = rightIdx;
            }

            if (smallest === index) break;              // 자식 노드보다 작으면 종료
            this.#heap[index] = this.#heap[smallest];   // 자식 노드와 위치 교환
            index = smallest;
        }

        this.#heap[index] = node; // 마지막 위치에 노드 삽입
    }
}

function solution(priorities, location) {
    // 우선순위와 인덱스를 함께 큐에 저장
    const queue = priorities.map((priority, index) => [index, priority]); // (인덱스, 우선순위)
    const pq = new PriorityQueue();

    // 우선순위 큐에 (우선순위 * -1, 인덱스) 형태로 저장 (최대 힙 역할)
    for (let [_, priority] of queue) {
        pq.push(-priority, priority);  // 우선순위 반전
    }

    let executedCount = 0;

    // 큐가 빌 때까지 반복
    while (queue.length) {
        const [currentIdx, currentPriority] = queue.shift();

        // 현재 프로세스의 우선순위가 최고 우선순위와 같다면 실행
        if (currentPriority === pq.peek()) {
            pq.pop();                 // 우선순위 큐에서 제거
            executedCount++;          // 실행된 프로세스 개수 증가

            if (currentIdx === location) {
                return executedCount; // 찾던 프로세스면 실행 순서 반환
            }
        } else {
            queue.push([currentIdx, currentPriority]); // 다시 큐 뒤로
        }
    }
}

// ✅ 테스트 예제 실행
console.log(solution([2, 1, 3, 2], 2));  // 1
console.log(solution([1, 1, 9, 1, 1, 1], 0));  // 5