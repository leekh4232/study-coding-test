class Solution {
    public static String solution(String myString) {
        String answer = myString.toLowerCase();
        return answer;
    }

    public static void main(String[] args) {
        System.out.println(solution("aBcDeFg"));
        System.out.println(solution("aaa"));
    }
}