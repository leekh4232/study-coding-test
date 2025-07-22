import java.util.Arrays;

public class Solution {
    public static int[] solution(int[] numList) {
        int n = numList.length;

        // 리스트의 절반만 순회하며 양 끝 요소 교환
        for (int i = 0; i < n / 2; i++) {
            int p = n - i - 1; // 반대쪽 인덱스
            int temp = numList[i];
            numList[i] = numList[p];
            numList[p] = temp;
        }

        return numList; // 뒤집힌 배열 반환
    }

    public static void main(String[] args) {
        System.out.println(Arrays.toString(solution(new int[]{1, 2, 3, 4, 5})));  // [5, 4, 3, 2, 1]
        System.out.println(Arrays.toString(solution(new int[]{1, 1, 1, 1, 2})));  // [2, 1, 1, 1, 1]
    }
}