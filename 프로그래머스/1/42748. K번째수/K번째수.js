function solution(array, commands) {
    // 결과를 저장할 배열 초기화
    let answer = [];

    // commands 배열을 순회하면서 각 연산 수행
    for (let c of commands) {
        // i번째부터 j번째까지 슬라이싱하고 정렬
        let slice = array.slice(c[0] - 1, c[1]).sort((a, b) => a - b);
        // 정렬된 배열에서 k번째 요소를 선택하여 결과 배열에 추가
        answer.push(slice[c[2] - 1]);
    }

    // 최종 결과 반환
    return answer;
}

// ✅ 예제 테스트 실행
console.log(solution([1, 5, 2, 6, 3, 7, 4], [[2, 5, 3], [4, 4, 1], [1, 7, 3]]));
// 결과: [5, 6, 3]