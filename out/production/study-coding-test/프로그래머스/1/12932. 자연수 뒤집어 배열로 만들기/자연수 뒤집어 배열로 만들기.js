function solution(n) {
    // 1. 숫자를 문자열로 변환하여 배열로 저장
    let k = Array.from(String(n));

    // 2. 배열 크기 및 반절 위치 구하기
    let size = k.length;
    let half = Math.floor(size / 2);

    // 3. 배열을 직접 뒤집는 과정 (swap 방식)
    for (let i = 0; i < half; i++) {
        let p = size - i - 1;  // 반대쪽 인덱스 계산

        // 두 값을 교환 (swap)
        let a = k[i];
        k[i] = k[p];
        k[p] = a;
    }

    // 4. 문자열 배열을 정수 배열로 변환하여 반환
    return k.map(Number);
}

// ✅ 예제 테스트 실행
let n = 12345;
console.log(solution(n));  // 결과: [5, 4, 3, 2, 1]