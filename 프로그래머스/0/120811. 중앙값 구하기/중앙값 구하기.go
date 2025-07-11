func solution(array []int) int {
    var n int = len(array)
    
    for i:=0; i<n-1; i++ {
        for j:=i+1; j<n; j++ {
            if (array[i] > array[j]) {
                tmp := array[i]
                array[i] = array[j]
                array[j] = tmp
            }
        }
    }
    
    var mid int = n / 2
    
    return array[mid]
}