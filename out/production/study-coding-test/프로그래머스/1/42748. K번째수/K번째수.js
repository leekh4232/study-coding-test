function solution(array, commands) {
    // 결과를 저장할 배열 초기화
    let answer = [];

    // commands 배열을 순회하면서 각 명령에 대해 작업 수행
    for (let c of commands) {
        // 배열에서 c[0]번째부터 c[1]번째까지 잘라낸다
        // JavaScript에서 slice는 시작 인덱스를 포함하고, 종료 인덱스는 포함하지 않으므로
        // c[0] - 1부터 c[1]까지 지정해야 정확한 구간을 추출할 수 있다
        let slice = array.slice(c[0] - 1, c[1]);

        // 잘라낸 배열을 숫자 오름차순으로 정렬
        // (a, b) => a - b를 써야 숫자 기준으로 정확하게 정렬된다
        slice.sort((a, b) => a - b);

        // 정렬된 배열에서 c[2]번째 요소를 꺼낸다
        // 배열 인덱스는 0부터 시작하므로 c[2] - 1로 접근해야 함
        answer.push(slice[c[2] - 1]);
    }

    // 모든 명령에 대한 결과가 저장된 배열을 반환
    return answer;
}

// ✅ 예제 테스트 실행
console.log(solution(
    [1, 5, 2, 6, 3, 7, 4],
    [[2, 5, 3], [4, 4, 1], [1, 7, 3]]
));
// 출력 결과: [5, 6, 3]
