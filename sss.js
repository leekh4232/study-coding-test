import PriorityQueue from './PriorityQueue.js';

const pqueue = new PriorityQueue();

pqueue.push(2, 'CCC');
pqueue.push(3, 'BBB');
pqueue.push(1, 'AAA');

console.log(`큐 사이즈: ${pqueue.size()}`);   	// 3
console.log(`최상단 요소: ${pqueue.peek()}`);  		// AAA

const item1 = pqueue.pop();
console.log(`추출한 요소: ${item1}`);      		// AAA
console.log(`큐 사이즈: ${pqueue.size()}`);   	// 2
console.log(`최상단 요소: ${pqueue.peek()}`);  		// CCC

const item2 = pqueue.pop();
console.log(`추출한 요소: ${item2}`);        	// CCC
console.log(`큐 사이즈: ${pqueue.size()}`);     	// 1
console.log(`최상단 요소: ${pqueue.peek()}`);    	// BBB
