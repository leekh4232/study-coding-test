public class Solution {

    // 메인 메서드 - 테스트 실행
    public static void main(String[] args) {
        System.out.println(solution(10)); // 5
        System.out.println(solution(15)); // 8
    }

    // 합성수 개수를 구하는 메서드
    public static int solution(int n) {
        // 합성수의 개수를 저장할 변수 초기화
        int answer = 0;

        // 1부터 n까지 반복하면서 각 숫자가 합성수인지 판별
        for (int i = 1; i <= n; i++) {
            // i의 약수 개수를 세는 변수 초기화
            int count = 0;

            // 1부터 i까지 반복하면서 약수 개수 확인
            for (int j = 1; j <= i; j++) {
                // i가 j로 나누어 떨어지면 약수
                if (i % j == 0) {
                    // 약수 개수 증가
                    count++;

                    // 약수의 개수가 3개 이상이면 합성수
                    if (count >= 3) {
                        // 합성수 개수 증가
                        answer++;
                        // 더 이상 검사할 필요 없으므로 반복 종료
                        break;
                    }
                }
            }
        }

        // 계산된 합성수 개수 반환
        return answer;
    }
}