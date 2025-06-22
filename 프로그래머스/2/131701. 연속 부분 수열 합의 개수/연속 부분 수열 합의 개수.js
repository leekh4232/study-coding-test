function solution(elements) {
    // 중복 제거를 위한 집합 초기화
    const res = new Set();

    // 원래 수열의 길이
    const n = elements.length;

    // 원형 수열 처리를 위해 수열을 두 배로 확장
    const ext = elements.concat(elements);

    // 부분 수열의 길이를 1부터 n까지 증가시키며 탐색
    for (let size = 1; size <= n; size++) {
        // 초기 윈도우(부분 수열)의 합 계산
        let winSum = 0;
        for (let i = 0; i < size; i++) {
            winSum += elements[i];
        }

        // 초기 합을 결과 집합에 추가
        res.add(winSum);

        // 슬라이딩 윈도우 적용
        for (let i = 1; i < n; i++) {
            // 윈도우를 한 칸 이동하며 합 갱신
            winSum = winSum - ext[i - 1] + ext[i + size - 1];

            // 새로운 합을 결과 집합에 추가
            res.add(winSum);
        }
    }

    // 서로 다른 연속 부분 수열의 합 개수 반환
    return res.size;
}

// 테스트 케이스 실행
console.log(solution([7, 9, 1, 1, 4])); // 18