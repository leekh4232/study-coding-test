// i부터 j까지 k가 등장하는 횟수를 세는 Go 함수
func solution(i, j, k int) int {
	count := 0
	for n := i; n <= j; n++ {
		x := n
		if x == 0 && k == 0 {
			count++
		}
		for x > 0 {
			if x%10 == k {
				count++
			}
			x /= 10
		}
	}
	return count
}
