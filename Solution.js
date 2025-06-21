import Heap from './Heap.js';

// ✅ Python의 heapify 동작과 같은 코드
const data = [5, 1, 3, 2, 8, 7];
const heap = new Heap();

// 모든 요소를 힙에 삽입 (heapify와 동일한 효과)
data.forEach(num => heap.push(num));

for (let i = 0; i < data.length; i++) {
    // 힙에서 최상위 요소를 제거하고 출력
    console.log(heap.pop());
}