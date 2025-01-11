class Solution {
    public int[] solution(int[] prices) {
        // prices 배열의 길이를 n 변수에 저장한다.
        int n = prices.length;
        // 결과를 저장할 int[] answer 배열을 n 크기로 초기화한다.
        int[] answer = new int[n];

        // 이중 for문을 사용하여 주식 가격 유지 시간을 계산
        for (int i = 0; i < n; i++) {
            for (int j = i + 1; j < n; j++) {
                // 시간값을 1씩 증가
                answer[i]++;

                // 원래 값보다 낮아지면 가격이 떨어진 것이므로 시간 측정 중단
                if (prices[i] > prices[j]) {
                    break;
                }
            }
        }

        return answer;
    }
}