import java.util.*;

public class Solution {
    public static int[] solution(String[] keyinput, int[] board) {
        int x = 0, y = 0;
        int xlim = board[0] / 2;
        int ylim = board[1] / 2;

        for (String i : keyinput) {
            if (i.equals("right")) {
                if (x >= xlim) {
                    x = xlim;
                } else {
                    x += 1;
                }
            } else if (i.equals("left")) {
                if (x <= -xlim) {
                    x = -xlim;
                } else {
                    x -= 1;
                }
            } else if (i.equals("up")) {
                if (y >= ylim) {
                    y = ylim;
                } else {
                    y += 1;
                }
            } else if (i.equals("down")) {
                if (y <= -ylim) {
                    y = -ylim;
                } else {
                    y -= 1;
                }
            }
        }

        return new int[]{x, y};
    }

    // ✅ 예제 테스트 실행
    public static void main(String[] args) {
        System.out.println(Arrays.toString(solution(new String[]{"left", "right", "up", "right", "right"}, new int[]{11, 11}))); // [2, 1]
        System.out.println(Arrays.toString(solution(new String[]{"down", "down", "down", "down"}, new int[]{7, 9}))); // [0, -4]
    }
}
