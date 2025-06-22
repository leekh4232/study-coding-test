function solution(elements) {
    // 중복 제거할 집합 초기화
    const res = new Set();

    // 원본 배열 길이
    const n = elements.length;

    // 원형 처리용 배열 두 배 확장
    const ext = elements.concat(elements);

    // size = 부분 수열 길이
    for (let size = 1; size <= n; size++) {
        // 초기 구간 합 계산
        let winSum = 0;
        for (let k = 0; k < size; k++) {
            winSum += elements[k];
        }

        // 초기 합을 집합에 추가
        res.add(winSum);

        // 슬라이딩 윈도우 적용
        for (let i = 1; i < n; i++) {
            // 구간이동: 앞 값 제거, 뒤 새로운 값 추가
            winSum = winSum - ext[i - 1] + ext[i + size - 1];
            // 갱신된 합을 집합에 추가
            res.add(winSum);
        }
    }

    // 서로 다른 합의 개수 반환
    return res.size;
}

// 테스트
console.log(solution([7, 9, 1, 1, 4])); // 18