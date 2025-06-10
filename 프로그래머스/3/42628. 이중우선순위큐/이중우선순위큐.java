import java.util.*;

public class Solution {

    // 이중 우선순위 큐 연산을 수행하는 메서드
    public static int[] solution(String[] operations) {
        // TreeMap: key = 숫자, value = 해당 숫자의 개수
        TreeMap<Integer, Integer> map = new TreeMap<>();

        // 모든 연산 처리
        for (String op : operations) {
            // 연산 분리
            String[] parts = op.split(" ");
            String command = parts[0];
            int number = Integer.parseInt(parts[1]);

            // 삽입 연산
            if (command.equals("I")) {
                // 이미 존재하면 개수 증가, 없으면 1로 추가
                map.put(number, map.getOrDefault(number, 0) + 1);
            }

            // 삭제 연산
            else if (command.equals("D")) {
                if (map.isEmpty()) continue;

                int key = (number == 1) ? map.lastKey() : map.firstKey(); // 최댓값 또는 최솟값

                // 해당 키의 개수를 하나 줄이거나 제거
                if (map.get(key) == 1) {
                    map.remove(key);
                } else {
                    map.put(key, map.get(key) - 1);
                }
            }
        }

        // 결과 반환
        if (map.isEmpty()) {
            return new int[]{0, 0};
        } else {
            return new int[]{map.lastKey(), map.firstKey()};
        }
    }

    // 테스트 케이스 실행
    public static void main(String[] args) {
        String[] case1 = {"I 16", "I -5643", "D -1", "D 1", "D 1", "I 123", "D -1"};
        String[] case2 = {"I -45", "I 653", "D 1", "I -642", "I 45", "I 97", "D 1", "D -1", "I 333"};

        System.out.println(Arrays.toString(solution(case1))); // [0, 0]
        System.out.println(Arrays.toString(solution(case2))); // [333, -45]
    }
}
