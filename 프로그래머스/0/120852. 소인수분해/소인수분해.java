import java.util.*;

public class Solution {

    public static List<Integer> solution(int n) {
        List<Integer> answer = new ArrayList<>();
        int k = 2;

        while (n > 1) {
            if (n % k == 0) {
                answer.add(k);
                while (n % k == 0) {
                    n /= k;
                }
            }
            k++;
        }

        return answer;
    }

    // ✅ 테스트 실행
    public static void main(String[] args) {
        System.out.println(solution(12));   // [2, 3]
        System.out.println(solution(17));   // [17]
        System.out.println(solution(60));   // [2, 3, 5]
    }
}
