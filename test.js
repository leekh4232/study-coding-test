function solution(correct, submission) {
    const pos = {};		// 정답 순서 맵핑: 해전 이름 → 정답 인덱스
    correct.forEach((name, index) => {
        pos[name] = index;
    });

    const n = correct.length;
    let point = 0;

    // 모든 i < j 쌍을 순회하며 순서쌍 점수 계산
    for (let i = 0; i < n - 1; i++) {
        for (let j = i + 1; j < n; j++) {
            if (pos[submission[i]] < pos[submission[j]]) {
                point++;
            }
        }
    }

    const total = (n * (n - 1)) / 2;

    return `${point}/${total}`; // "point/total" 문자열로 결과 반환
}

// 테스트 실행
console.log(solution(
    ['okpo', 'sacheon', 'hansan', 'myeongnyang', 'noryang'],
    ['sacheon', 'hansan', 'myeongnyang', 'noryang', 'okpo']
)); // "6/10"

console.log(solution(
    ['alpha', 'beta', 'gamma'],
    ['alpha', 'gamma', 'beta']
)); // "2/3"

console.log(solution(
    ['naboo', 'geonosis', 'yavin', 'hoth', 'endor'],
    ['geonosis', 'yavin', 'hoth', 'endor', 'naboo']
)); // "6/10"
