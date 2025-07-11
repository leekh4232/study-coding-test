function solution(arr, divisor) {
    // 1. filter를 사용하여 divisor로 나누어 떨어지는 원소만 선택
    let result = arr.filter(num => num % divisor === 0);

    // 2. 결과 배열이 비어 있으면 [-1] 반환
    if (result.length === 0) {
        return [-1];
    }

    // 3. 결과 배열을 오름차순으로 정렬
    result.sort((a, b) => a - b);

    return result;
}

// ✅ 예제 테스트 실행
console.log(solution([1, 5, 9, 7, 10], 5));   // [5, 10]
console.log(solution([2, 36, 1, 3], 1));      // [1, 2, 3, 36]
console.log(solution([3, 2, 6], 10));         // [-1]
console.log(solution([3, 2, 6], 2));          // [2, 6]