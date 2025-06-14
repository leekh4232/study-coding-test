class PriorityQueue {
<<<<<<< HEAD
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

export default PriorityQueue;
=======
    #heap = new Array(64);
    #size = 0;

    size() {
        return this.#size;
    }

    peek() {
        console.log(this.#heap);
        return this.#heap[1];
    }

    push(value) {
        const heap = this.#heap;
        const size = ++this.#size;

        if (size === heap.length) heap.length *= 2;

        heap[size] = value;
        this.percolateUp();
    }

    percolateUp() {
        const heap = this.#heap;
        const size = this.#size;

        let pos = size;
        const item = heap[pos];

        while (pos > 1) {
            const parent = heap[Math.floor(pos / 2)];
            if (parent <= item) break;
            heap[pos] = parent;
            pos = Math.floor(pos / 2);
        }

        heap[pos] = item;
    }

    pop() {
        const value = this.#heap[1];
        if (value === undefined) return undefined;
        const size = --this.#size;

        this.#heap[1] = this.#heap[size + 1];
        this.#heap[size + 1] = undefined;
        this.percolateDown();
        return value;
    }

    percolateDown() {
        let pos = 1;
        const item = this.#heap[pos];

        while (pos * 2 <= this.#size) {
            let childIndex = pos * 2 + 1;
            if (childIndex > this.#size || this.#heap[pos * 2] < this.#heap[childIndex]) childIndex = pos * 2;
            const child = this.#heap[childIndex];
            if (item <= child) break;
            this.#heap[pos] = child;
            pos = childIndex;
        }

        this.#heap[pos] = item;
    }
}

export default PriorityQueue;
>>>>>>> 070a002b8c3022df1ab54a25396a98196ac84857
