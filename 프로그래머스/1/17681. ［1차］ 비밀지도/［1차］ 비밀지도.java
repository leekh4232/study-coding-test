// https://school.programmers.co.kr/learn/courses/30/lessons/17681
class Solution {
    public String[] solution(int n, int[] arr1, int[] arr2) {
        // n 크기의 문자열 배열 answer를 선언한다.
        // 이 배열은 최종적으로 완성된 지도의 각 행을 저장한다.
        String[] answer = new String[n];

        // 지도의 각 행에 대해 반복한다.
        // i는 현재 처리 중인 지도의 행 인덱스를 나타낸다.
        for (int i = 0; i < n; i++) {
            // arr1[i]와 arr2[i]를 비트 OR 연산한다.
            // 이 연산 결과는 두 지도 중 하나라도 벽(1)이면 최종적으로 벽(1)임을 나타낸다.
            // Integer.toBinaryString() 메소드를 사용하여 결과를 이진수 문자열로 변환한다.
            String binaryString = Integer.toBinaryString(arr1[i] | arr2[i]);

            // binaryString의 길이가 n보다 작을 경우, 앞에 '0'을 채워 n 길이에 맞춘다.
            // String.format()을 사용하여 문자열을 n 길이로 맞추고, 남는 공간은 공백으로 채운다.
            // replace() 메소드를 사용하여 채워진 공백을 '0'으로 변경한다.
            String paddedString = String.format("%" + n + "s", binaryString).replace(' ', '0');

            // paddedString에서 '1'을 '#'으로, '0'을 ' '으로 변환한다.
            // 이는 이진수 지도를 실제 지도 모양으로 변환하는 과정이다.
            String mapRow = paddedString.replaceAll("1", "#").replaceAll("0", " ");

            // 변환된 지도 행을 answer 배열의 현재 인덱스에 저장한다.
            answer[i] = mapRow;
        }
        // 모든 행에 대한 변환이 완료된 answer 배열을 반환한다.
        return answer;
    }
}