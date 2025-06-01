class PriorityQueue {
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
