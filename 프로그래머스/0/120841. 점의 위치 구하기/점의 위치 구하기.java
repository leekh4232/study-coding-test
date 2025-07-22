class Solution {
    public static int solution(int[] dot) {
        int answer = 0; // 사분면 값을 저장할 변수 초기화

        if (dot[0] > 0 && dot[1] > 0) {       // 1사분면
            answer = 1;
        } else if (dot[0] < 0 && dot[1] > 0) { // 2사분면
            answer = 2;
        } else if (dot[0] < 0 && dot[1] < 0) { // 3사분면
            answer = 3;
        } else if (dot[0] > 0 && dot[1] < 0) { // 4사분면
            answer = 4;
        }

        return answer; // 판별된 사분면 반환
    }

    public static void main(String[] args) {
        // 테스트 예제 실행
        System.out.println(solution(new int[]{2, 4}));   // 1
        System.out.println(solution(new int[]{-7, 9}));  // 2
    }
}