class Solution {
    static int maxSheep = 0;

    // 백트래킹 함수: 현재 상태에서 이동 가능한 노드를 모두 탐색하며 최대 양을 모은다
    public void backtracking(int[] info, int[][] edges, boolean[] visited, int sheep, int wolf) {
        // 양이 늑대보다 많을 경우에만 유효한 상태이므로 탐색 계속
        if (sheep > wolf) {
            // 현재 양의 수를 최대값과 비교하여 갱신
            maxSheep = Math.max(maxSheep, sheep);
        } else {
            // 늑대가 같거나 많아지는 순간 모든 양이 잡히므로 중단
            return;
        }

        // 간선 정보를 순회하면서 현재 방문한 노드와 연결된 자식 노드를 탐색
        for (int[] edge : edges) {
            int parent = edge[0];
            int child = edge[1];

            // 부모 노드는 방문했고 자식 노드는 방문하지 않은 경우만 탐색
            if (visited[parent] && !visited[child]) {
                // 자식 노드를 방문 처리
                visited[child] = true;

                // 자식 노드가 양일 경우 양 수 증가
                if (info[child] == 0) {
                    backtracking(info, edges, visited, sheep + 1, wolf);
                }
                // 자식 노드가 늑대일 경우 늑대 수 증가
                else {
                    backtracking(info, edges, visited, sheep, wolf + 1);
                }

                // 백트래킹 시 자식 노드 방문 여부 원복
                visited[child] = false;
            }
        }
    }

    // 문제 해결 메인 함수
    public int solution(int[] info, int[][] edges) {
        maxSheep = 0;
        // 각 노드 방문 여부를 저장하는 배열
        boolean[] visited = new boolean[info.length];

        // 루트 노드(0번)는 항상 양이며, 처음 방문 처리
        visited[0] = true;
        // 백트래킹 시작: 루트 노드 기준, 양 1마리, 늑대 0마리
        backtracking(info, edges, visited, 1, 0);

        // 탐색 중 저장된 결과 중 가장 큰 양 수를 반환
        return maxSheep;
    }

    public static void main(String[] args) {
        Solution sol = new Solution();

        int[] info1 = {0,0,1,1,1,0,1,0,1,0,1,1};
        int[][] edges1 = {{0,1},{1,2},{1,4},{0,8},{8,7},{9,10},{9,11},{4,3},{6,5},{4,6},{8,9}};
        System.out.println(sol.solution(info1, edges1)); // 출력: 5

        int[] info2 = {0,1,0,1,1,0,1,0,0,1,0};
        int[][] edges2 = {{0,1},{0,2},{1,3},{1,4},{2,5},{2,6},{3,7},{4,8},{6,9},{9,10}};
        System.out.println(sol.solution(info2, edges2)); // 출력: 5
    }
}