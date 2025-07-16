function solution(n, arr1, arr2) {
    // 최종적으로 완성된 지도의 각 행을 저장할 배열
    const answer = [];

    // 지도의 각 행에 대해 반복
    for (let i = 0; i < n; i++) {
        // arr1[i]와 arr2[i]를 비트 OR 연산하고 이진수 문자열로 변환
        const binary = (arr1[i] | arr2[i]).toString(2);

        // 이진수 문자열의 길이가 n보다 작을 경우, 앞에 '0'을 채워 길이를 맞춤
        const padded = binary.padStart(n, '0');

        // '1'을 '#'으로, '0'을 ' '으로 변환하여 지도 행을 생성
        // replaceAll 또는 정규식을 사용
        const mapRow = padded.replace(/1/g, '#').replace(/0/g, ' ');

        // 변환된 지도 행을 answer 배열에 추가
        answer.push(mapRow);
    }
    
    // 모든 행에 대한 변환이 완료된 answer 배열을 반환
    return answer;
}