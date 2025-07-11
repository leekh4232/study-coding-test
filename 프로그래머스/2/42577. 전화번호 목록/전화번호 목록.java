import java.util.HashMap;

public class Solution {

    // 전화번호 목록에서 접두어 관계가 존재하는지 확인하는 메서드
    public static boolean solution(String[] phoneBook) {
        // 전화번호를 키로 저장할 해시맵 생성
        HashMap<String, Integer> hashMap = new HashMap<>();

        // 모든 전화번호를 해시맵에 저장 (값은 의미 없음)
        for (String number : phoneBook) {
            hashMap.put(number, 1);
        }

        // 각 전화번호에 대해 접두어를 만들어가며 확인
        for (String number : phoneBook) {
            // 접두어를 담을 문자열 초기화
            String prefix = "";

            // 전화번호의 각 문자(숫자)를 순차적으로 더하며 접두어 생성
            for (int i = 0; i < number.length(); i++) {
                // 접두어에 현재 문자 추가
                prefix += number.charAt(i);

                // 접두어가 해시맵에 존재하고, 자기 자신은 아닐 때
                if (hashMap.containsKey(prefix) && !prefix.equals(number)) {
                    // 접두어 관계가 존재하므로 false 반환
                    return false;
                }
            }
        }

        // 접두어 관계가 없으면 true 반환
        return true;
    }

    // 테스트 케이스 실행을 위한 main 메서드
    public static void main(String[] args) {
        // 테스트 케이스 1
        System.out.println(solution(new String[]{"119", "97674223", "1195524421"})); // false

        // 테스트 케이스 2
        System.out.println(solution(new String[]{"123", "456", "789"})); // true

        // 테스트 케이스 3
        System.out.println(solution(new String[]{"12", "123", "1235", "567", "88"})); // false
    }
}
