import java.util.Scanner; 

public class Solution { 
    public static void main(String[] args) { 
        // Scanner 객체 생성 (표준 입력을 받기 위함)
        Scanner sc = new Scanner(System.in); 
        
        // 첫 번째 정수 입력
        int a = sc.nextInt(); 
        
        // 두 번째 정수 입력
        int b = sc.nextInt(); 
        
        // 형식에 맞게 두 정수의 합을 출력
        System.out.printf("%d + %d = %d", a, b, a + b); 
        
        // Scanner 객체 닫기 (자원 해제)
        sc.close(); 
    }
}
