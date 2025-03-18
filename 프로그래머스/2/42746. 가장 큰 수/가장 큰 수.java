import java.util.Arrays;

public class Solution {
    public String solution(int[] numbers) {
        // 숫자를 문자열로 변환
        String[] numStrs = Arrays.stream(numbers)
                .mapToObj(String::valueOf) // 각 숫자를 문자열로 변환
                .toArray(String[]::new); // 문자열 배열로 변환

        // 숫자를 조합했을 때 더 큰 값이 앞에 오도록 정렬
        Arrays.sort(numStrs, (a, b) -> (b + a).compareTo(a + b));

        // 정렬된 문자열 배열을 하나의 문자열로 합침
        String result = String.join("", numStrs);

        // '000' 같은 경우를 대비하여 첫 번째 문자가 '0'이면 "0"을 반환
        return result.startsWith("0") ? "0" : result;
    }

    public static void main(String[] args) {
        Solution sol = new Solution();

        // 예제 테스트 실행
        System.out.println(sol.solution(new int[]{6, 10, 2}));
        // 출력 결과: "6210"

        System.out.println(sol.solution(new int[]{3, 30, 34, 5, 9}));
        // 출력 결과: "9534330"
    }
}