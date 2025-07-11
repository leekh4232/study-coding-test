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