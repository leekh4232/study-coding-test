// 배열을 왼쪽 또는 오른쪽으로 한 칸씩 회전하는 Go 함수
func solution(numbers []int, direction string) []int {
	lenN := len(numbers)
	answer := make([]int, lenN)
	if direction == "right" {
		answer[0] = numbers[lenN-1]
		for i := 0; i < lenN-1; i++ {
			answer[i+1] = numbers[i]
		}
	} else if direction == "left" {
		for i := 1; i < lenN; i++ {
			answer[i-1] = numbers[i]
		}
		answer[lenN-1] = numbers[0]
	}
	return answer
}
