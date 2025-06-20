// 최대한 다양한 종류의 폰켓몬을 선택할 때의 최대 종류 수를 반환하는 함수
function solution(nums) {
  // nums 배열을 Set으로 변환하여 중복 제거
  const uniqueSet = new Set(nums);

  // 선택할 수 있는 최대 개수 계산 (N/2)
  const limit = nums.length / 2;

  // 고유한 종류 수와 limit 중 작은 값을 반환
  return uniqueSet.size > limit ? limit : uniqueSet.size;
}

// 테스트 케이스 실행
console.log(solution([3, 1, 2, 3]));        // 2
console.log(solution([3, 3, 3, 2, 2, 4])); // 3
console.log(solution([3, 3, 3, 2, 2, 2])); // 2