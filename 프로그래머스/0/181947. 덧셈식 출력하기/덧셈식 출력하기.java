// Scanner 클래스를 사용하기 위해 import
import java.util.Scanner; 

// Solution 클래스 정의
public class Solution { 

    // main 메서드는 프로그램 실행의 시작점
    public static void main(String[] args) { 
        // Scanner 객체 생성 (표준 입력을 받기 위함)
        Scanner sc = new Scanner(System.in); 
        
        // 첫 번째 정수를 입력받아 변수 a에 저장
        int a = sc.nextInt(); 
        
        // 두 번째 정수를 입력받아 변수 b에 저장
        int b = sc.nextInt(); 
        
        // printf를 사용해 "a + b = c" 형태로 출력
        System.out.printf("%d + %d = %d", a, b, a + b); 
        
        // Scanner 객체 닫기 (자원 해제)
        sc.close(); 
    }
}
