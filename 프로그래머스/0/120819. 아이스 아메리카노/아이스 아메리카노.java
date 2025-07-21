class Solution {
    public int[] solution(int money) {
        int cups = money / 5500;    // 최대 잔 수
        int change = money % 5500;  // 남은 잔돈

        return new int[]{cups, change};
    }
}