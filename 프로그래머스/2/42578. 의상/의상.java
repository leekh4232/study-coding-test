import java.util.HashMap;

public class Solution {

    // 서로 다른 옷의 조합 수를 계산하는 메서드
    public static int solution(String[][] clothes) {
        // 의상 종류별 개수를 저장할 해시맵 초기화
        HashMap<String, Integer> hashMap = new HashMap<>();

        // 의상 정보를 순회하며 종류별 개수 누적
        for (String[] item : clothes) {
            String name = item[0]; // 의상 이름 (사용되지 않음)
            String type = item[1]; // 의상 종류

            // 해당 종류가 이미 있으면 1 증가, 없으면 1로 초기화
            hashMap.put(type, hashMap.getOrDefault(type, 0) + 1);
        }

        // 의상 조합의 총 가짓수를 계산 (초기값은 곱셈을 위한 1)
        int answer = 1;

        // 각 종류마다 (입는 경우 수 + 입지 않는 경우 1)을 곱함
        for (String type : hashMap.keySet()) {
            answer *= (hashMap.get(type) + 1);
        }

        // 아무 종류의 옷도 입지 않은 경우(공집합) 1가지를 제외
        return answer - 1;
    }

    // 테스트 케이스 실행을 위한 main 메서드
    public static void main(String[] args) {
        // 테스트 케이스 1
        String[][] clothes1 = {
            {"crowmask", "face"},
            {"bluesunglasses", "face"},
            {"smoky_makeup", "face"}
        };
        System.out.println(solution(clothes1)); // 출력: 5

        // 테스트 케이스 2
        String[][] clothes2 = {
            {"crow_mask", "face"},
            {"blue_sunglasses", "face"},
            {"smoky_makeup", "face"}
        };
        System.out.println(solution(clothes2)); // 출력: 3
    }
}
