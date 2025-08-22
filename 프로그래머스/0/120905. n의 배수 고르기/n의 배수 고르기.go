func solution(n int, numlist []int) []int {
	answer := make([]int, 0, len(numlist))
	for i := range numlist {
		if numlist[i]%n == 0 {
			answer = append(answer, numlist[i])
		}
	}
	return answer
}