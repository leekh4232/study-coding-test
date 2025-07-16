function solution(data, col, rowBegin, rowEnd) {
    // data 배열을 정렬한다.
    // sort 메서드에 비교 함수를 전달하여 사용자 정의 정렬 기준을 정의한다.
    data.sort((row1, row2) => {
        // 첫 번째 정렬 기준: col-1번째 컬럼의 값을 오름차순으로 비교한다.
        // col-1은 0-based 인덱스에 맞추기 위함이다.
        if (row1[col - 1] !== row2[col - 1]) {
            return row1[col - 1] - row2[col - 1];
        }
        // 두 번째 정렬 기준: col-1번째 컬럼의 값이 같을 경우,
        // 첫 번째 컬럼(0번째)의 값을 내림차순으로 비교한다.
        return row2[0] - row1[0];
    });

    // 최종 결과를 저장할 변수를 0으로 초기화한다.
    let answer = 0;
    
    // rowBegin부터 rowEnd까지의 각 행에 대해 반복한다.
    // rowBegin과 rowEnd는 1-based 인덱스이므로, 0-based 인덱스를 위해 1을 빼준다.
    // for 루프의 조건은 'i < rowEnd'로 설정하여 rowEnd-1까지 반복하도록 한다.
    for (let i = rowBegin - 1; i < rowEnd; i++) {
        // 현재 처리 중인 행의 1-based 번호를 계산한다.
        const rowNumber = i + 1;
        
        // 현재 행의 모든 원소를 순회하며 rowNumber로 나눈 나머지들의 합(S_i)을 계산한다.
        // reduce 메서드를 사용하여 배열의 모든 원소를 하나의 값으로 축소한다.
        const si = data[i].reduce((sum, element) => {
            return sum + (element % rowNumber);
        }, 0); // 초기 sum 값을 0으로 설정한다.
        
        // 만약 현재 행이 범위 내의 첫 번째 행이라면 (즉, i가 rowBegin - 1과 같다면),
        // si 값을 answer에 직접 할당한다.
        if (i === rowBegin - 1) {
            answer = si;
        } 
        // 첫 번째 행이 아니라면,
        // 현재 si 값을 기존 answer와 비트와이즈 XOR 연산하여 answer를 갱신한다.
        else {
            answer ^= si;
        }
    }
    
    // 모든 계산이 완료된 후 최종 answer 값을 반환한다.
    return answer;
}