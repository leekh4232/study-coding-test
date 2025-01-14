/**
 * 프로그래머스 12932번 - 자연수 뒤집어 배열로 만들기
 * https://school.programmers.co.kr/learn/courses/30/lessons/12932
 */
import java.util.Arrays;

public class Solution {
    public int[] solution(long n) {
        /**
        // [풀이1] 특정 위치의 원소와 교환할 반대쪽 위치를 계산하는 형태
        char[] c = String.valueOf(n).toCharArray();
        int size = c.length;
        int half = size / 2;

        for (int i=0; i<half; i++) {
            int p = size - i - 1;

            char temp = c[i];
            c[i] = c[p];
            c[p] = temp;
        }

        int[] answer = new int[size];
        for (int i=0; i<size; i++) {
            answer[i] = c[i] - '0';
        }
        return answer;
        /*/
        // [풀이2] StringBuilder 클래스의 reverse() 메소드를 사용하는 형태
        String str = new StringBuilder(String.valueOf(n)).reverse().toString();
        return str.chars().map(c -> c - '0').toArray();
        /**/
    }

    public static void main(String[] args) {
        int n = 12345;
        int[] result = new Solution().solution(n);
        System.out.println(Arrays.toString(result));
    }
}