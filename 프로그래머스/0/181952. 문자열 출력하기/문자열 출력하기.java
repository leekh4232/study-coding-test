// Scanner 클래스를 사용하기 위해 import
import java.util.Scanner;

// Solution 클래스 정의
public class Solution {

    // main 메서드는 프로그램의 시작점
    public static void main(String[] args) {
        // Scanner 객체를 생성하여 표준 입력(System.in)을 받음
        Scanner sc = new Scanner(System.in);

        // 공백 없는 문자열을 한 줄로 입력받아 변수 a에 저장
        String a = sc.next();

        // 사용이 끝난 Scanner 객체를 닫아 자원을 해제함
        sc.close();

        // 입력받은 문자열 a를 출력함
        System.out.println(a);
    }
}
