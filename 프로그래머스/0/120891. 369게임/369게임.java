class Solution {
    public int solution(int order) {
        int answer = 0;  // 박수를 칠 횟수를 저장할 변수

        // 숫자를 문자열로 변환하여 각 자리수를 분석
        String orderStr = String.valueOf(order);

        // 문자열을 순회하면서 각 자리의 숫자를 확인
        for (char c : orderStr.toCharArray()) {
            // '3', '6', '9' 중 하나라면 카운트 증가
            if (c == '3' || c == '6' || c == '9') {
                answer++;  
            }
        }

        return answer;  // 최종적으로 박수를 칠 횟수 반환
    }

    // 테스트 코드
    public static void main(String[] args) {
        Solution sol = new Solution();
        System.out.println(sol.solution(3));      // 1 (3이 포함됨)
        System.out.println(sol.solution(29423));  // 2 (9와 3이 포함됨)
    }
}
