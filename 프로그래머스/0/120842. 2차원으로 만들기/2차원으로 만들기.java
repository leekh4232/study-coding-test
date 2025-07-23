import java.util.*;

public class Solution {
    public static List<List<Integer>> solution(int[] num_list, int n) {
        List<List<Integer>> answer = new ArrayList<>();

        int count = num_list.length / n;

        for (int i = 0; i < count; i++) {
            List<Integer> sublist = new ArrayList<>();
            for (int j = 0; j < n; j++) {
                sublist.add(num_list[n * i + j]);
            }
            answer.add(sublist);
        }

        return answer;
    }

    // ✅ 예제 테스트 실행
    public static void main(String[] args) {
        System.out.println(solution(new int[]{1, 2, 3, 4, 5, 6, 7, 8, 9}, 2));
        System.out.println(solution(new int[]{100, 95, 2, 4, 5, 6, 18, 33, 948}, 3));
    }
}
