public class Solution {
    public static int solution(int[][] board) {
        // 8방향 탐색 (상, 하, 좌, 우, 대각선)
        int[] dr = {-1, 1, 0, 0, -1, -1, 1, 1};
        int[] dc = {0, 0, -1, 1, -1, 1, -1, 1};

        int n = board.length;

        // 위험지역 설정 (지뢰 주변)
        for (int i = 0; i < n; i++) {
            for (int j = 0; j < n; j++) {
                if (board[i][j] == 1) {
                    for (int k = 0; k < 8; k++) {
                        int nr = i + dr[k];
                        int nc = j + dc[k];

                        // 범위 확인 + 위험지역 표시 (0 → 2)
                        if (nr >= 0 && nr < n && nc >= 0 && nc < n && board[nr][nc] == 0) {
                            board[nr][nc] = 2;
                        }
                    }
                }
            }
        }

        // 안전한 지역(0)의 개수 카운트
        int answer = 0;
        for (int i = 0; i < n; i++) {
            for (int j = 0; j < n; j++) {
                if (board[i][j] == 0) {
                    answer++;
                }
            }
        }

        return answer;
    }

    // ✅ 예제 테스트 실행
    public static void main(String[] args) {
        int[][] board1 = {
            {0, 0, 0, 0, 0},
            {0, 0, 0, 0, 0},
            {0, 0, 0, 0, 0},
            {0, 0, 1, 0, 0},
            {0, 0, 0, 0, 0}
        };
        System.out.println(solution(board1)); // 16

        int[][] board2 = {
            {0, 0, 0, 0, 0},
            {0, 0, 0, 0, 0},
            {0, 0, 0, 0, 0},
            {0, 0, 1, 1, 0},
            {0, 0, 0, 0, 0}
        };
        System.out.println(solution(board2)); // 13

        int[][] board3 = {
            {1, 1, 1, 1, 1, 1},
            {1, 1, 1, 1, 1, 1},
            {1, 1, 1, 1, 1, 1},
            {1, 1, 1, 1, 1, 1},
            {1, 1, 1, 1, 1, 1},
            {1, 1, 1, 1, 1, 1}
        };
        System.out.println(solution(board3)); // 0
    }
}
