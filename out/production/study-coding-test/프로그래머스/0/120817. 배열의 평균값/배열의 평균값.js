function solution(numbers) {
    var answer = 0;
    let sum = 0;
    let n = numbers.length;
    
    for (let i=0; i<numbers.length; i++) {
        sum += numbers[i];
    }
    
    answer = sum / n;
    
    return answer;
}