function solution(numbers) {
    // 숫자 배열의 각 요소를 문자열로 변환
    // 문자열로 변환해야 붙였을 때의 크기 비교가 가능함
    numbers = numbers.map(String);

    // 문자열을 내림차순으로 정렬
    // 정렬 기준은 문자열을 반복해서 비교하는 방식 (3자리 이상 차이나는 경우 대비)
    numbers.sort((a, b) => (b + b + b).localeCompare(a + a + a));

    // 정렬된 문자열들을 모두 이어 붙여 하나의 문자열로 만듦
    let result = numbers.join('');

    // 예외 처리: 모두 0으로 구성된 경우를 처리하기 위해 BigInt를 사용
    // 예: '000' → BigInt('000') → 0 → String(0) → '0'
    return String(BigInt(result));
}

// ✅ 예제 테스트 실행
console.log(solution([6, 10, 2]));
// 출력 결과: "6210"

console.log(solution([3, 30, 34, 5, 9]));
// 출력 결과: "9534330"
