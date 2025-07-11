function solution(want, number, discount) {
    // 요청 상품과 수량을 해시맵으로 구성
    const wantDict = {};
    for (let i = 0; i < want.length; i++) {
        wantDict[want[i]] = number[i];
    }

    // 슬라이딩 윈도우 크기: 요청한 상품의 총 수량 (예: 항상 10)
    const windowSize = number.reduce((acc, v) => acc + v, 0);
    let count = 0;

    // 가능한 모든 윈도우 시작 지점 탐색
    for (let i = 0; i <= discount.length - windowSize; i++) {
        // 현재 윈도우 부분 배열 추출
        const window = discount.slice(i, i + windowSize);

        // 윈도우 내 상품 수량을 해시맵으로 계산
        const windowCounter = {};
        for (const item of window) {
            if (windowCounter[item] === undefined) {
                windowCounter[item] = 1;
            } else {
                windowCounter[item]++;
            }
        }

        // 모든 요청 상품이 충분히 포함되었는지 확인
        let isValid = true;
        for (const item in wantDict) {
            if (!windowCounter[item] || windowCounter[item] < wantDict[item]) {
                isValid = false;
                break;
            }
        }

        // 조건 만족 시 count 증가
        if (isValid) {
            count++;
        }
    }

    // 결과 반환
    return count;
}

// 테스트 실행
console.log(
    solution(
        ["banana", "apple", "rice", "pork", "pot"],
        [3, 2, 2, 2, 1],
        [
            "chicken", "apple", "apple", "banana", "rice",
            "apple", "pork", "banana", "pork", "rice", "pot",
            "banana", "apple", "banana"
        ]
    )
); // 3

console.log(
    solution(
        ["apple"],
        [10],
        Array(10).fill("banana")
    )
); // 0
