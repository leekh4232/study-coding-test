func solution(n int, t int) int {
	tPow := 1
	for i := 1; i <= t; i++ {
		tPow *= 2
	}
	return n * tPow
}