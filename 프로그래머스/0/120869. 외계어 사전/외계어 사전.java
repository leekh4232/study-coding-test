import java.util.Arrays;

public class Solution {

    public static int solution(String[] spell, String[] dic) {
        // spell 배열을 알파벳 순으로 정렬
        Arrays.sort(spell);
        String joinedSpell = String.join("", spell);

        for (String word : dic) {
            // 단어를 문자 배열로 변환한 후 정렬
            String[] chars = word.split("");
            Arrays.sort(chars);
            String sortedWord = String.join("", chars);

            // spell과 동일한 문자 조합인지 비교
            if (joinedSpell.equals(sortedWord)) {
                return 1;
            }
        }

        return 2;
    }

    // ✅ 테스트 실행
    public static void main(String[] args) {
        System.out.println(solution(new String[]{"p", "o", "s"},
                                     new String[]{"sod", "eocd", "qixm", "adio", "soo"})); // 2

        System.out.println(solution(new String[]{"z", "d", "x"},
                                     new String[]{"def", "dww", "dzx", "loveaw"})); // 1

        System.out.println(solution(new String[]{"s", "o", "m", "d"},
                                     new String[]{"moos", "dzx", "smm", "sunmmo", "som"})); // 2
    }
}
