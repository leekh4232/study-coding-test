// 우선순위 큐 시뮬레이션을 통해 특정 프로세스의 실행 순서를 구하는 함수
function solution(priorities, location) {
    // 실행된 프로세스 수를 저장할 변수
    let answer = 0;

    // priorities 배열을 순회하면서 각 프로세스의 우선순위와 원래 인덱스를 객체로 저장
    const array = priorities.map((process, index) => {
        return { process, index };
    });

    // 큐가 빌 때까지 반복
    while (array.length) {
        // 큐의 맨 앞 프로세스를 꺼냄
        const queue = array.shift();

        // 큐에 queue.process보다 더 높은 우선순위가 있는지 확인
        if (array.some((element) => element.process > queue.process)) {
            // 더 높은 우선순위가 있으면 꺼낸 프로세스를 큐의 뒤로 보냄
            array.push(queue);
        } else {
            // 그렇지 않으면 프로세스를 실행
            answer++;

            // 실행된 프로세스가 찾고자 하는 위치(location)인지 확인
            if (queue.index === location) break;
        }
    }

    // 찾고자 하는 프로세스의 실행 순서를 반환
    return answer;
}

// ✅ 테스트 예제 실행
console.log(solution([2, 1, 3, 2], 2)); // 1
console.log(solution([1, 1, 9, 1, 1, 1], 0)); // 5
