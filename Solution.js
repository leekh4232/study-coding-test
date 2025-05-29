class PriorityQueue {
    constructor() {
        this.heap = [];
    }

    // 요소 추가: [priority, value] 형태
    push(priority, value) {
        const node = { priority, value };
        this.heap.push(node);
        this.#bubbleUp();
    }

    // 우선순위가 가장 높은 요소 꺼내기
    pop() {
        if (this.size() === 0) return null;
        const top = this.heap[0];
        const last = this.heap.pop();

        if (this.size() !== 0) {
            this.heap[0] = last;
            this.#sinkDown();
        }

        return top;
    }

    // 최상위 요소 확인
    peek() {
        return this.heap[0] || null;
    }

    // 큐 크기 확인
    size() {
        return this.heap.length;
    }

    // 내부 정렬: 위로 올림
    #bubbleUp() {
        let index = this.heap.length - 1;
        const node = this.heap[index];

        while (index > 0) {
            const parentIdx = Math.floor((index - 1) / 2);
            if (this.heap[parentIdx].priority <= node.priority) break;

            this.heap[index] = this.heap[parentIdx];
            index = parentIdx;
        }

        this.heap[index] = node;
    }

    // 내부 정렬: 아래로 내림
    #sinkDown() {
        let index = 0;
        const length = this.heap.length;
        const node = this.heap[0];

        while (true) {
            const leftIdx = 2 * index + 1;
            const rightIdx = 2 * index + 2;
            let smallest = index;

            if (leftIdx < length && this.heap[leftIdx].priority < this.heap[smallest].priority) {
                smallest = leftIdx;
            }
            if (rightIdx < length && this.heap[rightIdx].priority < this.heap[smallest].priority) {
                smallest = rightIdx;
            }

            if (smallest === index) break;

            this.heap[index] = this.heap[smallest];
            index = smallest;
        }

        this.heap[index] = node;
    }
}
