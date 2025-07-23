public class Solution {
    public static int solution(int[][] dots) {
        // 가능한 세 가지 직선 조합을 직접 설정하여 기울기 비교
        int[][] case1 = {dots[0], dots[1], dots[2], dots[3]};
        int[][] case2 = {dots[0], dots[2], dots[1], dots[3]};
        int[][] case3 = {dots[0], dots[3], dots[1], dots[2]};

        int[][][] cases = {case1, case2, case3};

        for (int[][] pair : cases) {
            int x1 = pair[0][0], y1 = pair[0][1];
            int x2 = pair[1][0], y2 = pair[1][1];
            int x3 = pair[2][0], y3 = pair[2][1];
            int x4 = pair[3][0], y4 = pair[3][1];

            // 두 직선의 기울기 비교
            if ((y1 - y2) * (x3 - x4) == (y3 - y4) * (x1 - x2)) {
                return 1;  // 평행한 직선 존재
            }
        }

        return 0;  // 평행한 직선 없음
    }

    // ✅ 예제 테스트 실행
    public static void main(String[] args) {
        System.out.println(solution(new int[][]{{1, 4}, {9, 2}, {3, 8}, {11, 6}})); // 결과: 1
        System.out.println(solution(new int[][]{{3, 5}, {4, 1}, {2, 4}, {5, 10}})); // 결과: 0
    }
}
