import java.util.HashMap;

public class Solution {

    // 완주하지 못한 참가자를 찾는 메서드
    public static String solution(String[] participant, String[] completion) {
        // 해시값을 키로, 이름을 값으로 저장할 HashMap 생성
        HashMap<Integer, String> hashMap = new HashMap<>();

        // 참가자 해시값의 총합을 저장할 변수
        int sumHash = 0;

        // 참가자 배열을 순회하며 해시값을 누적하고 Map에 저장
        for (String part : participant) {
            // 현재 참가자의 해시값 계산
            int h = part.hashCode();

            // 해시값을 키로, 이름을 값으로 저장
            hashMap.put(h, part);

            // 해시값을 총합에 더함
            sumHash += h;
        }

        // 완주자 배열을 순회하며 해시값을 총합에서 차감
        for (String comp : completion) {
            // 현재 완주자의 해시값 계산
            int h = comp.hashCode();

            // 해시값을 총합에서 빼기
            sumHash -= h;
        }

        // 남은 해시값으로 완주하지 못한 참가자의 이름을 찾아 반환
        return hashMap.get(sumHash);
    }

    // 테스트 케이스 실행을 위한 main 메서드
    public static void main(String[] args) {
        // 테스트 케이스 1
        System.out.println(solution(
            new String[]{"leo", "kiki", "eden"},
            new String[]{"eden", "kiki"}
        )); // 출력: leo

        // 테스트 케이스 2
        System.out.println(solution(
            new String[]{"marina", "josipa", "nikola", "vinko", "filipa"},
            new String[]{"josipa", "filipa", "marina", "nikola"}
        )); // 출력: vinko

        // 테스트 케이스 3
        System.out.println(solution(
            new String[]{"mislav", "stanko", "mislav", "ana"},
            new String[]{"stanko", "ana", "mislav"}
        )); // 출력: mislav
    }
}
