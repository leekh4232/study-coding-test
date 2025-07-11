function solution(strings, n) {
    // 문자열 배열을 정렬하기 위해 sort 메서드 사용
    // 정렬 기준은 인덱스 n의 문자
    // 만약 n번째 문자가 같다면, 전체 문자열을 기준으로 사전순 정렬
    return strings.sort((a, b) => {
        // 두 문자열의 n번째 문자가 같을 경우
        if (a[n] === b[n]) {
            // 전체 문자열을 사전순으로 비교하여 정렬
            return a.localeCompare(b);
        }
        // 두 문자열의 n번째 문자가 다를 경우
        // n번째 문자를 사전순으로 비교하여 정렬
        return a[n].localeCompare(b[n]);
    });
}

// ✅ 예제 테스트 실행
console.log(solution(["sun", "bed", "car"], 1));
// 출력 결과: ["car", "bed", "sun"]

console.log(solution(["abce", "abcd", "cdx"], 2));
// 출력 결과: ["abcd", "abce", "cdx"]
