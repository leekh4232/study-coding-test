function solution(arr, divisor) {
    // 1. 나누어 떨어지는 원소를 저장할 배열
    let result = [];

    // 2. 배열을 순회하면서 divisor로 나누어 떨어지는 숫자만 선택
    for (let num of arr) {
        if (num % divisor === 0) {
            result.push(num);
        }
    }

    // 3. 결과 배열이 비어 있다면 [-1] 반환
    if (result.length === 0) {
        return [-1];
    }

    // 4. 결과를 오름차순 정렬하여 반환
    result.sort((a, b) => a - b);

    return result;
}

// ✅ 예제 테스트 실행
console.log(solution([5, 9, 7, 10], 5));   // 결과: [5, 10]
console.log(solution([2, 36, 1, 3], 1));   // 결과: [1, 2, 3, 36]
console.log(solution([3, 2, 6], 10));      // 결과: [-1]
console.log(solution([3, 2, 6], 2));       // 결과: [2, 6]