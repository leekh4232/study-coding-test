function solution(numbers) {
    const answer = [];
    
    for (const number of numbers) {
        // BigInt로 변환하여 계산
        const num = BigInt(number);

        // num이 짝수인 경우
        if (num % 2n === 0n) {
            // 가장 오른쪽 비트가 0이므로, +1하면 비트가 1개만 바뀐다.
            answer.push(num + 1n);
        } 
        // num이 홀수인 경우
        else {
            // num보다 크면서 비트가 1-2개 다른 가장 작은 수를 찾아야 한다.
            // 이는 이진수에서 가장 오른쪽에 있는 '0'을 '1'로 바꾸고,
            // 그 바로 오른쪽 '1'을 '0'으로 바꾸는 것과 같다.
            
            // 가장 오른쪽 0의 위치(자리값)를 찾는다.
            // 1. num과 num+1을 XOR 연산하면 가장 오른쪽 '0'과 그 오른쪽의 '1'이 모두 1로 바뀐다.
            const temp = (num ^ (num + 1n));
            // 2. 여기서 오른쪽으로 1 쉬프트하고 1을 더하면 가장 오른쪽 '0'의 자리값만 남는다.
            const rightmostZeroPos = (temp >> 1n) + 1n;
            
            // 원래 수에 (가장 오른쪽 0의 자리값 / 2)를 더한다.
            const result = num + (rightmostZeroPos / 2n);
            answer.push(result);
        }
    }
    
    // BigInt 결과를 다시 Number로 변환하여 반환 (문제의 반환 타입에 맞게)
    return answer.map(big => Number(big));
}