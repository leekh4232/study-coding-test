function solution(s) {
    // 제거 과정을 추적할 스택 초기화
    const stack = [];

    // 문자열을 처음부터 끝까지 순회
    for (let char of s) {
        // 스택이 비어 있지 않고, 스택 최상단 문자와 현재 문자가 같을 경우
        if (stack.length && stack[stack.length - 1] === char) {
            // 쌍을 이루는 문자이므로 스택에서 제거 (pop)
            stack.pop();
        } else {
            // 쌍이 아니므로 현재 문자를 스택에 추가
            stack.push(char);
        }
    }

    // 스택이 비어 있으면 모든 문자가 제거되었으므로 1, 아니면 0 반환
    return stack.length === 0 ? 1 : 0;
}

// ✅ 예제 테스트 실행
console.log(solution("baabaa"));  // 결과: 1
console.log(solution("cdcd"));    // 결과: 0
