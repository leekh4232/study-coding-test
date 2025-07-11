function solution(s) {
    // 괄호 짝을 판단할 스택 초기화
    let stack = [];

    // 문자열을 처음부터 끝까지 순회
    for (let char of s) {
        // 여는 괄호는 스택에 추가
        if (char === '(') {
            stack.push(char);
        }
        // 닫는 괄호가 나왔을 경우
        else if (char === ')') {
            // 스택이 비어 있다면 짝이 맞지 않음
            if (stack.length === 0) {
                return false;
            }
            // 가장 최근의 여는 괄호 제거
            stack.pop();
        }
    }

    // 스택이 비어 있으면 모든 괄호가 올바르게 닫힘 → true 반환
    // 스택이 남아 있으면 일부 괄호가 닫히지 않음 → false 반환
    return stack.length === 0;
}

// ✅ 예제 테스트 실행
console.log(solution("()()"));     // true
console.log(solution("(())()"));   // true
console.log(solution(")()("));     // false
console.log(solution("(()("));     // false
console.log(solution("()"));       // true
console.log(solution(")("));       // false
console.log(solution(")"));        // false
console.log(solution("("));        // false
console.log(solution("))"));       // false
console.log(solution("(("));       // false
