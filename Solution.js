import Heap from './Heap.js';

// 배열의 원소에 -1을 곱하여 최대 힙을 최소 힙으로 변환
// --> 최소 힙을 사용하여 최대 힙의 기능을 구현
const data = [5, 1, 3, 2, 8, 7];
const datamax = data.map(v => -v);
const heap = new Heap();

// 모든 요소를 힙에 삽입 (heapify와 동일한 효과)
datamax.forEach(num => heap.push(num));

for (let i = 0; i < data.length; i++) {
    // 힙에서 최상위 요소를 제거하고 출력시에는 다시 -1을 곱해야 함
    console.log(-heap.pop());
}