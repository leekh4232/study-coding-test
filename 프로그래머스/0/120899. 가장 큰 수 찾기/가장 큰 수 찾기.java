public class Solution {

    public static int[] solution(int[] array) {
        int maxValue = array[0];
        int maxIndex = 0;

        // 배열을 순회하면서 최대값과 인덱스를 찾음
        for (int i = 1; i < array.length; i++) {
            if (array[i] > maxValue) {
                maxValue = array[i];
                maxIndex = i;
            }
        }

        // 결과를 배열 형태로 반환
        return new int[] { maxValue, maxIndex };
    }

    // ✅ 테스트용 main 메서드
    public static void main(String[] args) {
        int[] result1 = solution(new int[] {1, 8, 3});
        int[] result2 = solution(new int[] {9, 10, 11, 8});

        System.out.println(java.util.Arrays.toString(result1)); // [8, 1]
        System.out.println(java.util.Arrays.toString(result2)); // [11, 2]
    }
}
