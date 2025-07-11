function solution(prices) {
    // 가격 배열의 길이를 저장
    const n = prices.length;

    // 결과를 저장할 배열을 0으로 초기화
    const answer = new Array(n).fill(0);

    // 가격이 떨어지지 않은 구간의 시작 인덱스를 저장할 스택
    const stack = [];

    // 각 시간 인덱스를 하나씩 확인
    for (let i = 0; i < n; i++) {
        const v = prices[i];

        // 현재 가격이 이전 가격보다 낮은 경우,
        // 스택에 저장된 인덱스를 꺼내며 유지된 시간을 계산
        while (stack.length && prices[stack[stack.length - 1]] > v) {
            const j = stack.pop();     // 이전 시점의 인덱스를 꺼냄
            answer[j] = i - j;         // 현재 시간과의 차이를 저장
        }

        // 현재 인덱스를 스택에 추가
        stack.push(i);
    }

    // 스택에 남은 인덱스들은 끝까지 가격이 떨어지지 않은 경우
    while (stack.length) {
        const j = stack.pop();
        answer[j] = n - 1 - j;         // 전체 남은 시간을 계산하여 저장
    }

    // 결과 배열 반환
    return answer;
}

// ✅ 예제 테스트 실행
console.log(solution([1, 2, 3, 2, 3]));  // 결과: [4, 3, 1, 1, 0]
