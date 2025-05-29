function solution(strings, n) {
    // 인덱스 n의 문자를 우선 기준으로 정렬, 같은 경우 원래 문자열을 기준으로 정렬
    return strings.sort((a, b) => {
        if (a[n] === b[n]) {
            return a.localeCompare(b); // 사전순 정렬
        }
        return a[n].localeCompare(b[n]); // n번째 문자 기준 정렬
    });
}

// ✅ 예제 테스트 실행
console.log(solution(["sun", "bed", "car"], 1));
// 결과: ["car", "bed", "sun"]

console.log(solution(["abce", "abcd", "cdx"], 2));
// 결과: ["abcd", "abce", "cdx"]
