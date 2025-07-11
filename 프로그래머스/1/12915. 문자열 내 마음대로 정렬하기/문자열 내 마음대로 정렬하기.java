import java.util.Arrays;
import java.util.List;
import java.util.stream.Collectors;

public class Solution { 
    public List<String> solution(String[] strings, int n) { 
        // 문자열 배열을 스트림으로 변환 후 정렬 수행
        List<String> answer = Arrays.stream(strings)
                .sorted((x, y) -> { 
                    // n번째 문자가 같으면 전체 문자열을 기준으로 정렬
                    if (x.charAt(n) == y.charAt(n)) { 
                        return x.compareTo(y); 
                    }
                    // n번째 문자를 기준으로 정렬
                    return Character.compare(x.charAt(n), y.charAt(n)); 
                })
                .collect(Collectors.toList()); // 리스트로 변환
        
        // 정렬된 결과 반환
        return answer; 
    }

    public static void main(String[] args) { 
        // 예제 테스트 실행
        Solution sol = new Solution(); 
        System.out.println(sol.solution(new String[]{"sun", "bed", "car"}, 1));
        // 출력 결과: ["car", "bed", "sun"]

        System.out.println(sol.solution(new String[]{"abce", "abcd", "cdx"}, 2));
        // 출력 결과: ["abcd", "abce", "cdx"]
    }
}
