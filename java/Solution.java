public class Solution {
    static int N, M;
    static List<List<Integer>> result = new ArrayList<>();
    static List<Integer> path = new ArrayList<>();

    public static List<List<Integer>> solution(int n, int m) {
        N = n;
        M = m;
        result.clear();
        path.clear();
        backtrack(0);  // 초기 visited 비트마스크는 0
        return result;
    }

    private static void backtrack(int visited) {
        if (path.size() == M) {
            result.add(new ArrayList<>(path));  // 결과 저장
            return;
        }

        for (int i = 1; i <= N; i++) {
            if ((visited & (1 << i)) == 0) {        // i를 아직 사용하지 않았다면
                path.add(i);                        // 경로에 추가
                backtrack(visited | (1 << i));      // 방문 처리 후 재귀 호출
                path.remove(path.size() - 1);       // 백트래킹
            }
        }
    }
}