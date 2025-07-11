class Solution {
    public int solution(String str1, String str2) {
        if (str1.indexOf(str2) != -1) { // str1에서 str2를 찾았을 때
            return 1; // 포함되면 1 반환
        } else {
            return 2; // 포함되지 않으면 2 반환
        }
    }

    // 테스트 예제 실행
    public static void main(String[] args) {
        Solution sol = new Solution();
        System.out.println(sol.solution("ab6CDE443fgh22iJKlmn1o", "6CD")); // 1
        System.out.println(sol.solution("ppprrrogrammers", "pppp")); // 2
        System.out.println(sol.solution("AbcAbcA", "AAA")); // 2
    }
}
