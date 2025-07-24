import java.util.ArrayList;
import java.util.List;

public class Solution {
    public static void main(String[] args) {
        int N = 3;
        List<Integer> path = new ArrayList<>();
        backtrack(path, 0, N); // 초기 visited = 0
    }

    public static void backtrack(List<Integer> path, int visited, int N) {
        if (path.size() == N) {
            System.out.println(path);
            return;
        }

        for (int i = 1; i <= N; i++) {
            // 아직 사용하지 않은 숫자인 경우
            if ((visited & (1 << i)) == 0) {
                path.add(i);                           // 경로에 추가
                visited |= (1 << i);                   // i 사용 표시
                backtrack(path, visited, N);           // 재귀 호출
                visited &= ~(1 << i);                  // i 사용 취소 (백트래킹)
                path.remove(path.size() - 1);          // 백트래킹
            }
        }
    }
}