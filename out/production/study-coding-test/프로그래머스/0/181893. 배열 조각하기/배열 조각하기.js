function solution(arr, query) {
    // 1. query 배열을 순회하면서 arr을 지속적으로 잘라냄
    for (let i = 0; i < query.length; i++) {
        if (i % 2 === 0) {  // 짝수 인덱스 → 뒷부분 제거
            arr = arr.slice(0, query[i] + 1);
        } else {  // 홀수 인덱스 → 앞부분 제거
            arr = arr.slice(query[i]);
        }
    }

    // 2. 최종적으로 남은 배열 반환
    return arr;
}

// ✅ 예제 테스트 실행
console.log(solution([0, 1, 2, 3, 4, 5], [4, 1, 2]));         // 결과: [1, 2, 3]
console.log(solution([10, 21, 32, 43, 54, 65], [4, 1, 2]));   // 결과: [21, 32, 43]