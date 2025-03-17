import java.util.Scanner; 

public class Solution { 
    public static void main(String[] args) { 
        // Scanner 객체 생성 (표준 입력을 받기 위함)
        Scanner sc = new Scanner(System.in); 
        
        // 공백이 없는 단일 문자열을 입력받음
        String a = sc.next();  
        
        // Scanner 객체 닫기 (자원 해제)
        sc.close(); 
        
        // 입력받은 문자열을 출력
        System.out.println(a);
    }
}
