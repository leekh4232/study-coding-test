import java.util.HashSet;

public class Solution {

    // 최대한 다양한 종류의 폰켓몬을 선택할 때의 최대 종류 수를 반환하는 메서드
    public static int solution(int[] nums) {
        // HashSet을 이용해 중복되지 않는 폰켓몬 종류를 저장
        HashSet<Integer> set = new HashSet<>();

        // nums 배열을 순회하면서 각 폰켓몬 번호를 집합에 추가
        for (int n : nums) {
            set.add(n);
        }

        // 선택 가능한 최대 폰켓몬 수는 전체의 절반
        int maxSelect = nums.length / 2;

        // 중복 제거한 종류 수와 maxSelect 중 더 작은 값을 반환
        return Math.min(set.size(), maxSelect);
    }

    // 테스트 케이스 실행을 위한 main 메서드
    public static void main(String[] args) {
        // 테스트 케이스 1
        System.out.println(solution(new int[]{3, 1, 2, 3})); // 출력: 2

        // 테스트 케이스 2
        System.out.println(solution(new int[]{3, 3, 3, 2, 2, 4})); // 출력: 3

        // 테스트 케이스 3
        System.out.println(solution(new int[]{3, 3, 3, 2, 2, 2})); // 출력: 2
    }
}
