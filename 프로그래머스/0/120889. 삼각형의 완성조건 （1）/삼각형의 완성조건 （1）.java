public class Solution {

    public static int solution(int[] sides) {
        int n = sides.length;

        // 선택 정렬을 사용하여 오름차순 정렬
        for (int i = 0; i < n - 1; i++) {
            for (int j = i + 1; j < n; j++) {
                if (sides[j] < sides[i]) {
                    // 교환
                    int temp = sides[i];
                    sides[i] = sides[j];
                    sides[j] = temp;
                }
            }
        }

        // 가장 긴 변이 나머지 두 변의 합보다 작으면 삼각형 가능
        if (sides[2] < sides[0] + sides[1]) {
            return 1;
        } else {
            return 2;
        }
    }

    public static void main(String[] args) {
        System.out.println(solution(new int[]{1, 2, 3}));       // 2
        System.out.println(solution(new int[]{3, 6, 2}));       // 2
        System.out.println(solution(new int[]{199, 72, 222}));  // 1
    }
}
