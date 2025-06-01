function solution(arr) {
    // 연속 중복을 제거한 결과를 저장할 스택 배열 생성
    let stack = [];

    // 입력 배열을 처음부터 끝까지 순회
    for (let num of arr) {
        // 스택이 비어있거나, 스택의 마지막 값과 현재 숫자가 다를 경우
        if (stack.length === 0 || stack[stack.length - 1] !== num) {
            // 현재 숫자를 스택에 추가
            stack.push(num);
        }
    }

    // 스택에 저장된 값들은 연속 중복이 제거된 최종 결과
    return stack;
}

// ✅ 예제 테스트 실행
console.log(solution([1, 1, 3, 3, 0, 1, 1]));  // 결과: [1, 3, 0, 1]
console.log(solution([4, 4, 4, 3, 3]));        // 결과: [4, 3]
