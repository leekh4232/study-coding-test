public class Solution {

    public static int[] solution(int[] numlist, int n) {
        int length = numlist.length;

        // 선택 정렬 구현
        for (int i = 0; i < length - 1; i++) {
            int minIdx = i;

            for (int j = i + 1; j < length; j++) {
                int diffJ = Math.abs(numlist[j] - n);
                int diffMin = Math.abs(numlist[minIdx] - n);

                if (diffJ < diffMin || (diffJ == diffMin && numlist[j] > numlist[minIdx])) {
                    minIdx = j;
                }
            }

            // swap
            int temp = numlist[i];
            numlist[i] = numlist[minIdx];
            numlist[minIdx] = temp;
        }

        return numlist;
    }

    // ✅ 테스트용 main 메서드
    public static void main(String[] args) {
        int[] result1 = solution(new int[]{1, 2, 3, 4, 5, 6}, 4);
        int[] result2 = solution(new int[]{10000, 20, 36, 47, 40, 6, 10, 7000}, 30);

        System.out.println(java.util.Arrays.toString(result1));  // [4, 5, 3, 6, 2, 1]
        System.out.println(java.util.Arrays.toString(result2));  // [36, 40, 20, 47, 10, 6, 7000, 10000]
    }
}
