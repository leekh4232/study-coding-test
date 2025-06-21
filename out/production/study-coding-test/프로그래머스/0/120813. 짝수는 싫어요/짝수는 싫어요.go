func solution(n int) []int {
    var arr []int
    
    for i:=1; i<=n; i+=2 {
        arr = append(arr, i)
    }
    
    return arr
}