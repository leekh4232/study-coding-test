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

            if (value >= parent) break;

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

// 최소 횟수로 모든 음식의 스코빌 지수를 K 이상으로 만드는 함수
function solution(S, K) {
    // 최소 힙 인스턴스 생성
    const heap = new Heap();

    // 모든 스코빌 지수를 힙에 삽입
    for (let i = 0; i < S.length; i++) {
        heap.push(S[i]);
    }

    // 섞은 횟수를 저장할 변수
    let cnt = 0;

    // 가장 작은 스코빌 지수가 K 이상이 될 때까지 반복
    while (heap.peek() < K) {
        // 음식을 두 개 이상 꺼낼 수 없으면 -1 반환
        if (heap.size() === 1) {
            return -1;
        }

        // 가장 맵지 않은 음식 꺼냄
        const first = heap.pop();

        // 두 번째로 맵지 않은 음식 꺼냄
        const second = heap.pop();

        // 새로운 음식의 스코빌 지수 계산
        const newFood = first + (second * 2);

        // 새로운 음식을 힙에 추가
        heap.push(newFood);

        // 섞은 횟수 증가
        cnt++;
    }

    // 모든 음식이 K 이상일 때 섞은 횟수 반환
    return cnt;
}

// 테스트 케이스 실행
console.log(solution([1, 2, 3, 9, 10, 12], 7));  // 2