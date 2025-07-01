<<<<<<< HEAD
function solution(numbers) {
    let result = 0;  // 좋은 수의 개수
    numbers.sort((a, b) => a - b);  // 오름차순 정렬

    for (let k = 0; k < numbers.length; k++) {
        let S = 0;
        let E = numbers.length - 1;
        const target = numbers[k];

        while (S < E) {
            if (S === k) {
                S += 1;
                continue;
            }
            if (E === k) {
                E -= 1;
                continue;
            }

            const sum = numbers[S] + numbers[E];

            if (sum < target) {
                S += 1;
            } else if (sum > target) {
                E -= 1;
            } else {
                result += 1;
                break;
=======
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
>>>>>>> 2d5e6daaa62727c12c14935c5d15d6efea6fa3a6
            }
        }
    }

<<<<<<< HEAD
    return result;
}

// 테스트 실행
console.log(solution([1, 2, 3, 4, 5, 6, 7, 8, 9, 10]));  // 출력: 8
=======
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
>>>>>>> 2d5e6daaa62727c12c14935c5d15d6efea6fa3a6
