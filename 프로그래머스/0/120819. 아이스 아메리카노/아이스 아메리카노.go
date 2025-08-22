func solution(money int) [2]int {
	cups := money / 5500
	change := money % 5500
	return [2]int{cups, change}
}