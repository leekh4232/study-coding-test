function findCombinations(arr, currentCombination, start, r, result) {
    // 1. 베이스 케이스: 현재 조합의 길이가 r과 같으면 결과에 추가하고 종료
    if (currentCombination.length === r) {
        result.push([...currentCombination]); // 현재 조합을 복사하여 결과에 추가
        return;
    }

    // 2. 재귀 단계: start 인덱스부터 배열 끝까지 탐색
    for (let i = start; i < arr.length; i++) {
        // 현재 원소를 임시 조합에 추가
        currentCombination.push(arr[i]);
        // 다음 원소를 찾기 위해 재귀 호출 (다음 탐색은 i + 1부터 시작)
        findCombinations(arr, currentCombination, i + 1, r, result);
        // 다음 탐색을 위해 현재 추가했던 원소를 제거
        currentCombination.pop();
    }
}

const arr = [1, 2, 3, 4];
const r = 2; // 2개의 원소로 이루어진 조합

// 최종 결과를 저장할 배열
const result = [];

// 완전 탐색 시작
findCombinations(arr, [], 0, r, result);

console.log(result);
// 출력 결과: [ [ 1, 2 ], [ 1, 3 ], [ 1, 4 ], [ 2, 3 ], [ 2, 4 ], [ 3, 4 ] ]
