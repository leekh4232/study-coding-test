// 부분 배열을 반환하는 Go 함수
func solution(numbers []int, num1 int, num2 int) []int {
    return numbers[num1 : num2+1]
}