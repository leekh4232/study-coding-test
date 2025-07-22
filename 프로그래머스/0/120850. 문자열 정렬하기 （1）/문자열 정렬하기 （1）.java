import java.util.*;

public class Solution {

    public static int[] solution(String my_string) {
        List<Integer> numbers = new ArrayList<>();

        // 문자열을 한 글자씩 확인
        for (int i = 0; i < my_string.length(); i++) {
            char c = my_string.charAt(i);
            if (Character.isDigit(c)) {
                numbers.add(c - '0');  // 문자 숫자를 정수로 변환
            }
        }

        // 오름차순 정렬
        Collections.sort(numbers);

        // List<Integer> → int[] 변환
        int[] result = new int[numbers.size()];
        for (int i = 0; i < numbers.size(); i++) {
            result[i] = numbers.get(i);
        }

        return result;
    }

    // ✅ 테스트 실행
    public static void main(String[] args) {
        System.out.println(Arrays.toString(solution("hi12392")));   // [1, 2, 2, 3, 9]
        System.out.println(Arrays.toString(solution("p2o4i8gj2"))); // [2, 2, 4, 8]
        System.out.println(Arrays.toString(solution("abcde0")));    // [0]
    }
}
