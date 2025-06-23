function solution(sequence, k) {
    // 시작 포인터를 0으로 초기화
    let s = 0;

    // 끝 포인터를 0으로 초기화
    let e = 0;

    // 현재 구간합을 첫 번째 원소로 초기화
    let p = sequence[0];

    // 최소 길이를 무한대로 초기화하여 이후 비교 기준으로 사용
    let minLength = Infinity;

    // 조건을 만족하는 가장 짧은 구간의 인덱스를 저장할 배열
    let answer = [];

    // 끝 포인터가 배열 범위를 넘지 않을 때까지 반복
    while (e < sequence.length) {
        // 현재 구간합이 k보다 작은 경우
        if (p < k) {
            // 끝 포인터를 오른쪽으로 이동
            e += 1;

            // 끝 포인터가 배열 범위를 벗어나지 않는 경우만 처리
            if (e < sequence.length) {
                // 구간합에 새로운 값을 추가
                p += sequence[e];
            }

        // 현재 구간합이 k보다 큰 경우
        } else if (p > k) {
            // 구간합에서 시작 포인터의 값을 제거
            p -= sequence[s];

            // 시작 포인터를 오른쪽으로 이동
            s += 1;

        // 현재 구간합이 k와 같은 경우
        } else {
            // 현재 구간의 길이 계산
            const currentLength = e - s;

            // 기존 최소 길이보다 짧다면 갱신
            if (currentLength < minLength) {
                minLength = currentLength;

                // 현재 구간의 시작과 끝 인덱스를 저장
                answer = [s, e];
            }

            // 시작 포인터의 값을 구간합에서 제거
            p -= sequence[s];

            // 시작 포인터를 오른쪽으로 이동
            s += 1;
        }
    }

    // 가장 짧은 구간의 시작과 끝 인덱스를 배열로 반환
    return answer;
}

// 테스트 케이스 실행
console.log(solution([1, 2, 3, 4, 5], 7));       // [2, 3]
console.log(solution([1, 1, 1, 2, 3, 4, 5], 5)); // [6, 6]
console.log(solution([2, 2, 2, 2, 2], 6));       // [0, 2]
