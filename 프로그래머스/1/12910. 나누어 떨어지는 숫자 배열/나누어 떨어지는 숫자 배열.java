/**
 * 프로그래머스 12910번 - 나누어 떨어지는 숫자 배열
 * https://school.programmers.co.kr/learn/courses/30/lessons/12910
 */
import java.util.ArrayList;
import java.util.Arrays;
import java.util.Collections;
import java.util.List;
import java.util.stream.Collectors;

public class Solution {
    public int[] solution(int[] arr, int divisor) {
        /**
        // [풀이1] ArrayList를 사용한 형태
        List<Integer> result = new ArrayList<>();

        for (int i=0; i<arr.length; i++) {
            if (arr[i] % divisor == 0) {
                result.add(arr[i]);
            }
        }

        //if (result.size() == 0) {
        if (result.isEmpty()) {
            result.add(-1);
        } else {
            Collections.sort(result);
        }

        return result.stream().mapToInt(i -> i).toArray();
        /*/
        // [풀이2] Stream을 사용하여 나누어 떨어지는 숫자 필터링
        List<Integer> result = Arrays.stream(arr)
                .filter(num -> num % divisor == 0) // 나누어 떨어지는 숫자만 필터링
                .sorted() // 정렬
                .boxed() // int -> Integer 변환
                .collect(Collectors.toList()); // 결과를 List로 변환

        if (result.isEmpty()) {
            result.add(-1);
        }

        return result.stream().mapToInt(i -> i).toArray();
        /**/
    }

    public static void main(String[] args) {
        Solution sol = new Solution();

        System.out.println(Arrays.toString(sol.solution(new int[]{5, 9, 7, 10}, 5))); // [5, 10]
        System.out.println(Arrays.toString(sol.solution(new int[]{2, 36, 1, 3}, 1)));    // [1, 2, 3, 36]
        System.out.println(Arrays.toString(sol.solution(new int[]{3, 2, 6}, 10)));       // [-1]
    }
}