function solution(numbers) {
    // 숫자를 문자열로 변환
    numbers = numbers.map(String);

    // 숫자를 3번 반복한 값을 기준으로 내림차순 정렬
    numbers.sort((a, b) => (b + b + b).localeCompare(a + a + a));

    // 정렬된 배열을 하나의 문자열로 합침
    let result = numbers.join('');

    // '000' 같은 경우를 대비하여 int로 변환 후 다시 문자열로 변환
    return String(BigInt(result));
}

// ✅ 예제 테스트 실행
console.log(solution([6, 10, 2]));        // 결과: "6210"
console.log(solution([3, 30, 34, 5, 9])); // 결과: "9534330"
