// 배열에서 n이 등장하는 횟수를 반환하는 Go 함수
func solution(array []int, n int) int {
	answer := 0
	for i := 0; i < len(array); i++ {
		if array[i] == n {
			answer++
		}
	}
	return answer
}
