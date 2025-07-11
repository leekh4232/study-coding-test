public class Solution {
    /**
     * 숫자야구 문제 해결 함수
     *
     * @param queries [[질문 숫자, 스트라이크 수, 볼 수], ...] 형태의 2차원 배열
     * @return 가능한 정답의 총 개수
     */
    public static int solution(int[][] queries) {
        int count = 0; // 가능한 정답의 개수를 세는 변수

        // 1. 모든 세 자리 수 후보를 생성하여 완전 탐색 (123 ~ 987)
        for (int cand = 123; cand <= 987; cand++) {
            String candStr = String.valueOf(cand);

            // 1. 후보 조건 검사
            // a. '0'이 포함된 경우 제외
            if (candStr.contains("0")) {
                continue;
            }
            // b. 중복된 숫자가 있는 경우 제외 (예: 112, 232)
            if (candStr.charAt(0) == candStr.charAt(1) ||
                    candStr.charAt(0) == candStr.charAt(2) ||
                    candStr.charAt(1) == candStr.charAt(2)) {
                continue;
            }

            // 2. 현재 후보가 모든 질문 조건을 만족하는지 확인
            boolean isPossible = true;
            for (int[] query : queries) {
                String guessStr = String.valueOf(query[0]);
                int expectedStrike = query[1], expectedBall = query[2];
                int strike = 0, ball = 0;

                // 3. 스트라이크와 볼 개수 계산
                for (int i = 0; i < 3; i++) {
                    for (int j = 0; j < 3; j++) {
                        // 같은 위치에 같은 숫자가 있으면 스트라이크
                        if (i == j && candStr.charAt(i) == guessStr.charAt(j)) {
                            strike++;
                        }
                        // 다른 위치에 같은 숫자가 있으면 볼
                        else if (i != j && candStr.charAt(i) == guessStr.charAt(j)) {
                            ball++;
                        }
                    }
                }

                // 4. 계산 결과가 예상과 다르면, 이 후보는 정답이 아님
                if (strike != expectedStrike || ball != expectedBall) {
                    isPossible = false;
                    break; // 다음 질문을 검사할 필요 없이 현재 후보 탐색 중단
                }
            }

            // 5. 모든 질문을 통과한 경우, 정답 개수 증가
            if (isPossible) {
                count++;
            }
        }

        return count;
    }

    // 테스트를 위한 main 함수
    public static void main(String[] args) {
        int[][] queries = { { 123, 1, 1 }, { 356, 1, 0 }, { 327, 2, 0 }, { 489, 0, 1 } };
        System.out.println(solution(queries)); // 예상 출력: 2
    }
}