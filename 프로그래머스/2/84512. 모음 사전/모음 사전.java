import java.util.ArrayList;
import java.util.List;

class Solution {
    // 사용할 모음 배열 정의
    static final char[] VOWELS = {'A', 'E', 'I', 'O', 'U'};
    
    // 백트래킹을 통해 가능한 모든 단어 조합을 생성하는 함수
    public void backtracking(String currentWord, List<String> wordList) {
        // 단어 길이가 5가 되면 종료 (더 이상 추가하지 않음)
        if (currentWord.length() == 5) {
            return;
        }

        // 모음 배열을 하나씩 붙여가며 재귀적으로 단어 생성
        for (int i = 0; i < VOWELS.length; i++) {
            // 현재 단어에 문자 추가
            String newWord = currentWord + VOWELS[i];
            // 완성된 단어를 리스트에 추가
            wordList.add(newWord);
            // 다음 글자를 붙이기 위해 재귀 호출
            backtracking(newWord, wordList);
        }
    }

    // 주어진 단어가 사전에서 몇 번째인지 반환하는 함수
    public int solution(String word) {
        // 단어 조합 결과를 저장할 리스트
        List<String> wordList = new ArrayList<>();
        // 백트래킹 시작: 빈 문자열에서 출발
        backtracking("", wordList);
        // word가 몇 번째 단어인지 반환 (1-based index)
        return wordList.indexOf(word) + 1;
    }

    // 테스트
    public static void main(String[] args) {
        Solution sol = new Solution();
        System.out.println(sol.solution("AAAAE"));    // 6
        System.out.println(sol.solution("AAAE"));     // 10
        System.out.println(sol.solution("I"));        // 1563
        System.out.println(sol.solution("EIO"));      // 1189
    }
}