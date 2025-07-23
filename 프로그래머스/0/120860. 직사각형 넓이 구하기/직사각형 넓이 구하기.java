public class Solution {

    public static int solution(int[][] dots) {
        int minX = dots[0][0];
        int maxX = dots[0][0];
        int minY = dots[0][1];
        int maxY = dots[0][1];

        // x, y 각각의 최댓값과 최솟값 계산
        for (int i = 1; i < dots.length; i++) {
            int x = dots[i][0];
            int y = dots[i][1];

            if (x < minX) minX = x;
            if (x > maxX) maxX = x;
            if (y < minY) minY = y;
            if (y > maxY) maxY = y;
        }

        int width = maxX - minX;
        int height = maxY - minY;

        return width * height;
    }

    // ✅ 테스트 실행
    public static void main(String[] args) {
        System.out.println(solution(new int[][]{{1, 1}, {2, 1}, {2, 2}, {1, 2}})); // 1
        System.out.println(solution(new int[][]{{-1, -1}, {1, 1}, {1, -1}, {-1, 1}})); // 4
    }
}
