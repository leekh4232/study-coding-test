func solution(balls int, share int) int {
	if share > balls-share {
		share = balls - share // 조합의 대칭성: C(balls, share) == C(balls, balls-share)
	}

	var result int64 = 1 // 결과값을 저장할 변수 (오버플로우 방지 위해 int64 사용)

	// (balls-share+1)부터 balls까지 곱하고, 동시에 1부터 share까지 나눠서 계산
	for i := 0; i < share; i++ {
		result *= int64(balls - i)
		result /= int64(i + 1)
	}

	return int(result) // 결과 반환
}