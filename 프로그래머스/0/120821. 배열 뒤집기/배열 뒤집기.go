// 배열을 뒤집는 Go 함수
func solution(numList []int) []int {
	n := len(numList)
	for i := 0; i < n/2; i++ {
		p := n - i - 1
		numList[i], numList[p] = numList[p], numList[i]
	}
	return numList
}