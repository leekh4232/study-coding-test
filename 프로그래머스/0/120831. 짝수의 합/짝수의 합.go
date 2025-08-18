func solution(n int) int {
	sum := 0 // 짝수들의 합을 저장할 변수 초기화
	// 1부터 n까지 반복하며 짝수인 경우만 합산
	for i := 1; i <= n; i++ {
		if i%2 == 0 { // 짝수인지 확인
			sum += i // 짝수일 경우 합산
		}
	}
	return sum // 최종적으로 누적된 짝수의 합 반환
}