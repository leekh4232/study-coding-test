public class Solution {
    public static int solution(String[] babbling) {
        // 발음할 수 있는 단어 리스트
        String[] words = {"aya", "ye", "woo", "ma"};
        int answer = 0;

        // 각 단어에 대해 검사
        for (String word : babbling) {
            for (String w : words) {
                word = word.replace(w, " ");  // 발음 가능한 단어를 공백으로 변환
            }
            if (word.trim().isEmpty()) {  // 모든 발음을 제거한 후 빈 문자열이면 발음 가능
                answer++;
            }
        }

        return answer;
    }

    // ✅ 예제 테스트 실행
    public static void main(String[] args) {
        System.out.println(solution(new String[]{"aya", "yee", "u", "maa", "wyeoo"})); // 결과: 1
        System.out.println(solution(new String[]{"ayaye", "uuuma", "ye", "yemawoo", "ayaa"})); // 결과: 3
    }
}
