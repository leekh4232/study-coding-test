import java.util.Scanner;

class Solution {
    public static void main(String[] args) {
        Scanner scanner = new Scanner(System.in);
        int n = scanner.nextInt(); // 사용자 입력값 n

        // 삼각형 출력
        for (int i = 1; i <= n; i++) { // i는 1부터 n까지 반복
            for (int j = 0; j < i; j++) { // j는 0부터 i-1까지 반복하며 "*" 출력
                System.out.print("*");
            }
            System.out.println(); // 줄바꿈
        }

        scanner.close();
    }
}