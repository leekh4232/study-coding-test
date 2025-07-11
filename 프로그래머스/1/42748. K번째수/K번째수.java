import java.util.ArrayList;
import java.util.List;
import java.util.Arrays;

public class Solution { 
    public List<Integer> solution(int[] array, int[][] commands) { 
        // 결과를 저장할 리스트 초기화
        List<Integer> answer = new ArrayList<>(); 

        // commands 배열을 순회하면서 각 연산 수행
        for (int[] c : commands) { 
            // 배열의 i번째부터 j번째까지 슬라이싱 (배열 인덱스는 0부터 시작하므로 c[0] - 1 사용)
            int[] slice = Arrays.copyOfRange(array, c[0] - 1, c[1]); 
            
            // 잘라낸 배열을 정렬
            Arrays.sort(slice); 
            
            // 정렬된 배열에서 k번째 요소를 결과 리스트에 추가 (배열 인덱스는 0부터 시작하므로 c[2] - 1 사용)
            answer.add(slice[c[2] - 1]); 
        }

        // 최종 결과 반환
        return answer;
    }

    public static void main(String[] args) { 
        // 예제 테스트 실행
        Solution sol = new Solution(); 
        System.out.println(sol.solution(
            new int[]{1, 5, 2, 6, 3, 7, 4}, 
            new int[][]{{2, 5, 3}, {4, 4, 1}, {1, 7, 3}}
        ));
        // 출력 결과: [5, 6, 3]
    }
}
