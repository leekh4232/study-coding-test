// 합성수 개수를 구하는 함수
func solution(n int) int {
	answer := 0 // 합성수의 개수를 저장할 변수 초기화
	for i := 1; i <= n; i++ {
		count := 0 // i의 약수 개수를 세는 변수 초기화
		for j := 1; j <= i; j++ {
			if i%j == 0 {
				count++
				if count >= 3 {
					answer++
					break
				}
			}
		}
	}
	return answer // 계산된 합성수 개수 반환
}