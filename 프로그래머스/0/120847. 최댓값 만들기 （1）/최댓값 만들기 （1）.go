// 배열에서 가장 큰 두 수의 곱을 반환하는 Go 함수
func solution(numbers []int) int {
	n := len(numbers)
	// 선택 정렬 (오름차순)
	for i := 0; i < n-1; i++ {
		for j := i + 1; j < n; j++ {
			if numbers[j] < numbers[i] {
				numbers[i], numbers[j] = numbers[j], numbers[i]
			}
		}
	}
	// 마지막 두 수의 곱이 최댓값
	return numbers[n-1] * numbers[n-2]
}
