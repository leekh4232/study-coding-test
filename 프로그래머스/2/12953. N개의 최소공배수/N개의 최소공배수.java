import java.util.*;

public class Solution {

    // 최소공배수 함수
    public static int lcm(int a, int b) {
        return Math.abs(a * b) / gcd(a, b);
    }

    // 최대공약수 함수
    public static int gcd(int a, int b) {
        if (b == 0) return a;
        return gcd(b, a % b);
    }

    // 재귀적으로 배열의 최소공배수를 구하는 함수
    public static int solution(int[] arr) {
        if (arr.length == 1) {
            return arr[0];
        } else {
            return lcm(arr[0], solution(Arrays.copyOfRange(arr, 1, arr.length)));
        }
    }

    public static void main(String[] args) {
        int[] arr = {2, 7, 3}; // 테스트 값
        System.out.println(solution(arr)); // 결과 출력
    }
}
