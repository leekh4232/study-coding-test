func solution(n int) int {
	x := 1
	for x*x <= n {
		if x*x == n {
			return 1
		}
		x++
	}
	return 2
}