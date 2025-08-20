package main

import "fmt"

func main() {
	var n int
	fmt.Scan(&n) // 사용자 입력값 n

	// 삼각형 출력
	for i := 1; i <= n; i++ {
		for j := 0; j < i; j++ {
			fmt.Print("*")
		}
		fmt.Println()
	}
}
