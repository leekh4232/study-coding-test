class Heap {
    // 내부 힙 배열
    #heap = [];

    // 요소 추가
    push(value) {
        this.#heap.push(value);
        this.#bubbleUp();
    }

    // 최상위 요소 제거 및 반환 (최소값)
    pop() {
        if (this.#heap.length === 0) return null;
        if (this.#heap.length === 1) return this.#heap.pop();

        const top = this.#heap[0];
        // 마지막 요소를 루트로 올림
        this.#heap[0] = this.#heap.pop();
        this.#sinkDown();
        return top;
    }

    // 최상위 요소 확인 (제거하지 않음)
    peek() {
        return this.#heap[0] ?? null;
    }

    // 현재 힙의 크기 반환
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

            if (value > parent) break;

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

            if (leftIndex < length && this.#heap[leftIndex] < this.#heap[smallest]) {
                smallest = leftIndex;
            }

            if (rightIndex < length && this.#heap[rightIndex] < this.#heap[smallest]) {
                smallest = rightIndex;
            }

            if (smallest === index) break;

            this.#heap[index] = this.#heap[smallest];
            this.#heap[smallest] = value;
            index = smallest;
        }
    }
}

export default Heap;
