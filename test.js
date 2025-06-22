import PriorityQueue from "./PriorityQueue.js";

function solution(xlist) {
    let myQueue = new PriorityQueue();      // 우선순위 큐 생성
    let answer = [];                        // 결과를 저장할 배열

    for (let x of xlist) {                  // 입력 배열을 순회
        if (x !== 0) {                      // 숫자가 0이 아니라면?
            myQueue.put([Math.abs(x), x]);  // 절댓값을 기준으로 큐에 숫자를 추가
        } else {                            // 숫자가 0이면
            if (myQueue.size() == 0) {      // 큐가 비어있으면
                answer.push(0);             // 결과 배열에 0 추가
            } else {                        // 큐가 비어있지 않으면
                let temp = myQueue.get();   // 큐에서 가장 작은 값을 꺼냄
                answer.push(temp[1]);       // 해당 값을 결과 배열에 추가
            }
        }
    }
    return answer;                          // 결과 배열을 반환
}
// -> [-1, 1, 0, -1, -1, 1, 1, -2, 2, 0]
console.log(solution([1, -1, 0, 0, 0, 1, 1, -1, -1, 2, -2, 0, 0, 0, 0, 0, 0, 0]));
