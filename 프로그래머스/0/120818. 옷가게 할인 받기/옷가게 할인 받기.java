class Solution {
    public int solution(int price) {
        if (price >= 500000) {
            return (int) (price * 0.8); // 20% 할인 적용
        } else if (price >= 300000) {
            return (int) (price * 0.9); // 10% 할인 적용
        } else if (price >= 100000) {
            return (int) (price * 0.95); // 5% 할인 적용
        } else {
            return price; // 할인 없음
        }
    }

    public static void main(String[] args) {
        Solution s = new Solution();

        // 테스트 예제 실행
        System.out.println(s.solution(150000)); // 142500
        System.out.println(s.solution(580000)); // 464000
    }
}
