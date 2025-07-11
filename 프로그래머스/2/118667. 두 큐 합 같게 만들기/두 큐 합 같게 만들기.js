function solution(queue1, queue2) {
    // queue1의 합 계산
    const sum1 = queue1.reduce((a, b) => a + b, 0);

    // queue2의 합 계산
    const sum2 = queue2.reduce((a, b) => a + b, 0);

    // 전체 합을 구함
    const total = sum1 + sum2;

    // 전체 합이 홀수이면 두 큐를 절반으로 나눌 수 없으므로 -1 반환
    if (total % 2 !== 0) {
        return -1;
    }

    // 목표 합은 전체 합의 절반
    const target = total / 2;

    // 두 큐를 합쳐 하나의 배열로 만듦 (원형 배열처럼 사용할 예정)
    const combined = queue1.concat(queue2);

    // queue1의 길이 저장
    const n = queue1.length;

    // 시작 포인터는 queue1의 시작을 가리킴
    let s = 0;

    // 끝 포인터는 queue2의 시작을 가리킴
    let e = n;

    // 현재 구간합은 queue1의 합으로 초기화
    let p = sum1;

    // 최대 이동 횟수는 두 큐의 길이의 합의 두 배로 설정
    const maxMoves = combined.length * 2;

    // 현재 이동 횟수
    let moves = 0;

    // 최대 이동 횟수 내에서 반복
    while (moves < maxMoves) {
        // 현재 구간합이 목표 값과 같으면 이동 횟수를 반환
        if (p === target) {
            return moves;
        }

        // 현재 구간합이 목표보다 작으면 오른쪽 값을 더함
        if (p < target) {
            p += combined[e];
            e += 1;

        // 현재 구간합이 목표보다 크면 왼쪽 값을 제거
        } else {
            p -= combined[s];
            s += 1;
        }

        // 이동 횟수 증가
        moves += 1;
    }

    // 목표 값을 만들 수 없는 경우 -1 반환
    return -1;
}

// 테스트 케이스 실행
console.log(solution([3, 2, 7, 2], [4, 6, 5, 1]));  // 2
console.log(solution([1, 2, 1, 2], [1, 10, 1, 2])); // 7
console.log(solution([1, 1], [1, 5]));             // -1
