public class Solution {
    public int solution(int hp) {
        // 장군개미 (5의 공격력) 사용 개수 계산
        int general = hp / 5;
        int remainder = hp % 5;  // 남은 체력
    
        // 병정개미 (3의 공격력) 사용 개수 계산
        int soldier = remainder / 3;
        int worker = remainder % 3;  // 남은 체력 (일개미가 담당)
    
        return general + soldier + worker;  // 총 개미 수 반환
    }

    public static void main(String[] args) {
        Solution s = new Solution();
        System.out.println(s.solution(23));
        System.out.println(s.solution(24));
        System.out.println(s.solution(999));
    }
}