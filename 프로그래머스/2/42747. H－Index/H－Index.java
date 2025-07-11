import java.util.Arrays;

public class Solution { 
    public int solution(int[] citations) { 
        // 인용 횟수를 오름차순 정렬
        Arrays.sort(citations); 
        int n = citations.length; // 논문의 개수

        // H-Index를 저장할 변수
        int answer = 0; 

        // 정렬된 리스트를 순회하며 H-Index 계산
        for (int i = 0; i < n; i++) { 
            int h = n - i; // 현재 논문의 인용 횟수가 (n - i)번 이상인지 확인
            if (citations[i] >= h) { 
                answer = h; // H-Index 업데이트
                break; // 조건을 만족하는 최대값을 찾으면 종료
            }
        }

        // 최종 H-Index 반환
        return answer; 
    }

    public static void main(String[] args) { 
        Solution sol = new Solution(); 
        
        // 예제 테스트 실행
        System.out.println(sol.solution(new int[]{3, 0, 6, 1, 5})); 
        // 출력 결과: 3 (H-Index)
    }
}
