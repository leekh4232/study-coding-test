import java.util.*;

class Solution {
    public int solution(int[] array) {
        int count = 0;  // 숫자 '7'의 개수를 저장할 변수

        // 배열의 모든 요소를 확인
        for (int num : array) {
            // 숫자를 문자열로 변환하여 '7'의 개수를 세기
            String numStr = String.valueOf(num);
            
            // 문자열을 순회하면서 '7'이 몇 번 등장하는지 확인
            for (char c : numStr.toCharArray()) {
                if (c == '7') {  // 문자가 '7'이면 카운트 증가
                    count++;
                }
            }
        }

        return count;  // 최종적으로 7이 등장한 횟수 반환
    }

    // 테스트 코드
    public static void main(String[] args) {
        Solution sol = new Solution();
        System.out.println(sol.solution(new int[]{7, 77, 17}));  // 4 ('7'이 4번 등장)
        System.out.println(sol.solution(new int[]{10, 29}));     // 0 ('7'이 없음)
    }
}
