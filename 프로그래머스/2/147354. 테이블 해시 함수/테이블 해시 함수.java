import java.util.Arrays; // 배열 정렬을 위해 Arrays 클래스를 임포트한다.
import java.util.Comparator; // 사용자 정의 정렬을 위해 Comparator 인터페이스를 임포트한다.

class Solution {
    public int solution(int[][] data, int col, int rowBegin, int rowEnd) {
        // data 배열을 정렬한다.
        // Comparator를 사용하여 사용자 정의 정렬 기준을 제공한다.
        Arrays.sort(data, new Comparator<int[]>() {
            @Override // Comparator 인터페이스의 compare 메서드를 오버라이드한다.
            public int compare(int[] row1, int[] row2) {
                // 첫 번째 정렬 기준: col-1번째 컬럼의 값을 오름차순으로 비교한다.
                // col-1은 0-based 인덱스에 맞추기 위함이다.
                if (row1[col - 1] != row2[col - 1]) {
                    return row1[col - 1] - row2[col - 1];
                }
                // 두 번째 정렬 기준: col-1번째 컬럼의 값이 같을 경우,
                // 첫 번째 컬럼(0번째)의 값을 내림차순으로 비교한다.
                return row2[0] - row1[0];
            }
        });

        // 최종 결과를 저장할 변수를 0으로 초기화한다.
        int answer = 0;
        
        // rowBegin부터 rowEnd까지의 각 행에 대해 반복한다.
        // rowBegin과 rowEnd는 1-based 인덱스이므로, 0-based 인덱스를 위해 1을 빼준다.
        // for 루프의 조건은 'i < rowEnd'로 설정하여 rowEnd-1까지 반복하도록 한다.
        for (int i = rowBegin - 1; i < rowEnd; i++) {
            // 현재 처리 중인 행의 1-based 번호를 계산한다.
            int rowNumber = i + 1;
            
            // 현재 행의 S_i 값을 저장할 변수를 0으로 초기화한다.
            int si = 0;
            // 현재 행 (data[i])의 각 원소를 반복하여 접근한다.
            for (int element : data[i]) {
                // 각 원소를 현재 행 번호로 나눈 나머지를 si에 더한다.
                si += (element % rowNumber);
            }
            
            // 만약 현재 행이 범위 내의 첫 번째 행이라면 (즉, i가 rowBegin - 1과 같다면),
            // si 값을 answer에 직접 할당한다.
            if (i == rowBegin - 1) {
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
}