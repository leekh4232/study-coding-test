class Solution {
    public int solution(int chicken) {
        int answer = 0; // 받을 수 있는 총 서비스 치킨 수

        while (chicken >= 10) { // 쿠폰이 10장 이상일 때만 교환 가능
            int service = chicken / 10; // 10개당 서비스 치킨 수 계산
            int remainder = chicken % 10; // 교환 후 남은 쿠폰 수 계산
            answer += service; // 총 서비스 치킨 수에 추가
            chicken = service + remainder; // 새로운 쿠폰 개수로 업데이트
        }

        return answer;
    }

    public static void main(String[] args) {
        Solution s = new Solution();

        // 테스트 예제 실행
        System.out.println(s.solution(100));  // 11
        System.out.println(s.solution(1081)); // 120
    }
}
