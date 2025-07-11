/**
 * 재귀를 이용해 순열을 생성하는 메인 함수
 * @param {number[]} nums - 순열을 만들 원본 숫자 배열
 * @returns {number[][]} - 모든 순열이 담긴 2차원 배열
 */
function permute(nums) {
    // 1. 모든 순열의 결과를 담을 배열
    const result = [];

    // 2. 완전 탐색을 위한 재귀 함수 호출
    findPermutations(result, [], nums, new Array(nums.length).fill(false));

    return result;
}

/**
 * 재귀적으로 모든 경우의 수를 탐색하여 순열을 생성하는 함수
 * @param {number[][]} result - 최종 결과를 담을 배열
 * @param {number[]} currentList - 현재 만들어지고 있는 하나의 순열
 * @param {number[]} nums - 원본 숫자 배열
 * @param {boolean[]} used - 각 숫자의 사용 여부 (true/false)
 */
function findPermutations(result, currentList, nums, used) {
    // [재귀 종료 조건] 하나의 순열이 완성되면 (예: 리스트가 3개 숫자로 모두 채워지면)
    if (currentList.length === nums.length) {
        // 결과 배열에 완성된 순열의 "복사본"을 추가하고 현재 탐색을 종료
        result.push([...currentList]);
        return;
    }

    // [재귀 호출을 통한 탐색] 원본 배열의 모든 숫자를 하나씩 확인하여 다음 자리에 넣어봄
    for (let i = 0; i < nums.length; i++) {
        // 만약 이미 현재 순열에 사용된 숫자라면 건너뜀
        if (used[i]) { continue; }

        // 1. 선택: 현재 숫자를 순열에 추가
        currentList.push(nums[i]);
        used[i] = true;

        // 2. 다음 자리 탐색: 다음 자리를 채우기 위해 재귀적으로 함수를 다시 호출
        findPermutations(result, currentList, nums, used);

        // 3. 상태 복원: 위 재귀 호출이 끝나면, 다음 경우의 수를 위해 상태를 원래대로 되돌림
        //    (마지막에 추가했던 숫자를 제거하고, '사용함' 표시도 해제)
        currentList.pop();
        used[i] = false;
    }
}

// 실행 코드
const arr = [1, 2, 3];
const result = permute(arr);
console.log(result);