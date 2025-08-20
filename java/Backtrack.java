import java.util.ArrayList;
import java.util.List;
import java.util.Arrays;

public class Backtrack {
    public static void main(String[] args) {
        int N = 3;
        boolean[] used = new boolean[N + 1]; // 인덱스 1~N 사용
        List<Integer> path = new ArrayList<>();
        backtrack(path, used, N);
    }

    public static void backtrack(List<Integer> path, boolean[] used, int N) {
        if (path.size() == N) {
            System.out.println("결과: " + path);
            return;
        }


        for (int i = 1; i <= N; i++) {
            if (!used[i]) {
                System.out.println("숫자 " + i + " 선택 전: " + path);

                used[i] = true; // 숫자 i 사용 표시
                System.out.println("(1) ---> " + Arrays.toString(used));
                path.add(i); // path에 추가
                System.out.println("숫자 " + i + " 선택 후: " + path);

                System.out.println("숫자 " + i + " 백트래킹 전: " + path);
                backtrack(path, used, N); // 재귀호출
                path.remove(path.size() - 1); // 백트래킹
                used[i] = false; // 백트래킹: 사용 취소
                System.out.println("(2) ---> " + Arrays.toString(used));
                System.out.println("숫자 " + i + " 백트래킹 후: " + path);
            }
        }
    }
}
