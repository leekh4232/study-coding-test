class Solution {
    public int solution(String A, String B) {
        String doubledB = B + B; // B 문자열을 두 번 이어붙여 새로운 문자열 생성

        int index = doubledB.indexOf(A); // A가 처음 등장하는 위치 찾기
        if (index != -1) {
            return index; // A가 포함되어 있으면 해당 위치 반환
        } else {
            return -1; // A가 포함되지 않으면 -1 반환
        }
    }

    // 테스트 예제 실행
    public static void main(String[] args) {
        Solution sol = new Solution();
        System.out.println(sol.solution("hello", "ohell")); // 1
        System.out.println(sol.solution("apple", "elppa")); // -1
        System.out.println(sol.solution("atat", "tata")); // 1
        System.out.println(sol.solution("abc", "abc")); // 0
    }
}
