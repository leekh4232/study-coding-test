class Solution {
    // 정답의 개수를 저장할 클래스 멤버 변수
    static int answer;
    // 방문 여부를 저장할 배열
    static boolean[] visited;

    // solution 함수는 입력받은 number 배열에서
    // 3개의 수를 선택해 합이 0이 되는 조합의 수를 찾는 함수
    public int solution(int[] number) {
        // 정답과 방문 배열 초기화
        answer = 0;
        visited = new boolean[number.length];

        // 백트래킹 탐색을 시작 (시작 인덱스 0, 선택된 개수 0, 합계 0)
        backtracking(0, 0, 0, number);

        // 모든 탐색이 끝난 후, answer에 저장된 정답 개수를 반환
        return answer;
    }

    // backtracking 함수는 현재 인덱스, 선택 개수, 누적 합, 원본 배열을 인자로 받음
    public void backtracking(int index, int depth, int total, int[] number) {
        // 만약 3개를 선택했다면
        if (depth == 3) {
            // 선택한 3개 원소의 합이 0이면 answer 증가
            if (total == 0) {
                answer++;
            }
            // 3개를 다 골랐으므로 더 이상 진행하지 않고 함수 종료
            return;
        }

        // index부터 배열 끝까지 반복
        for (int i = index; i < number.length; i++) {
            // 아직 방문하지 않은 인덱스라면
            if (!visited[i]) {
                // 해당 인덱스를 선택(방문)했다고 표시
                visited[i] = true;
                // 다음 단계로 재귀 호출 (i+1부터 시작, 선택 개수+1, 합에 현재 값 더함)
                backtracking(i + 1, depth + 1, total + number[i], number);
                // 백트래킹: 재귀가 끝나면 선택 해제(원상 복구)
                visited[i] = false;
            }
        }
    }

    public static void main(String[] args) {
        Solution sol = new Solution();
        // 예시 테스트 케이스 실행
        System.out.println(sol.solution(new int[]{-2, 3, 0, 2, -5}));        // 출력: 2
        System.out.println(sol.solution(new int[]{-3, -2, -1, 0, 1, 2, 3})); // 출력: 5
        System.out.println(sol.solution(new int[]{-1, 1, -1, 1}));           // 출력: 0
    }
}