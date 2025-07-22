import java.util.HashSet;

class Solution {
    // 찾은 소수들을 저장할 중복 없는 집합(Set)
    HashSet<Integer> resultSet = new HashSet<>();

    // 숫자가 소수인지 판별하는 함수
    public boolean isPrime(int num) {
        // 1 이하의 숫자는 소수가 아니다.
        if (num <= 1) {
            return false;
        }
        // 2는 소수이다.
        if (num == 2) {
            return true;
        }
        // 짝수는 소수가 아니다.
        if (num % 2 == 0) {
            return false;
        }
        // 3부터 숫자의 제곱근까지 홀수만으로 나누어 떨어지는지 확인한다.
        for (int i = 3; i <= Math.sqrt(num); i += 2) {
            if (num % i == 0) {
                return false;
            }
        }
        // 위 조건에 해당하지 않으면 소수이다.
        return true;
    }

    // 백트래킹을 수행하는 함수
    // currentNum: 현재까지 만들어진 숫자를 문자열 형태로 저장
    // numbers: 원본 숫자 문자열
    // visited: 이미 사용된 numbers의 인덱스를 저장하는 boolean 배열
    public void backtrack(String currentNum, String numbers, boolean[] visited) {
        // currentNum이 비어있지 않다면 (즉, 숫자가 생성되었다면)
        if (!currentNum.isEmpty()) {
            int num = Integer.parseInt(currentNum);
            // currentNum을 정수로 변환하여 소수인지 확인한다.
            if (isPrime(num)) {
                // 소수라면 resultSet에 추가한다.
                resultSet.add(num);
            }
        }

        // numbers의 각 숫자 조각에 대해 반복한다.
        for (int i = 0; i < numbers.length(); i++) {
            // 현재 인덱스 i의 숫자 조각이 아직 사용되지 않았다면
            if (!visited[i]) {
                // 방문 처리
                visited[i] = true;
                // 현재 숫자(currentNum)에 numbers[i]를 추가하여 재귀 호출
                backtrack(currentNum + numbers.charAt(i), numbers, visited);
                // 백트래킹: 재귀가 끝나면 방문 해제(원상 복구)
                visited[i] = false;
            }
        }
    }

    // 주어진 숫자 조각들로 만들 수 있는 소수의 개수를 찾는 함수
    public int solution(String numbers) {
        // 방문 여부 배열 초기화
        boolean[] visited = new boolean[numbers.length()];
        // 초기 호출: 빈 문자열과 방문 배열로 백트래킹을 시작한다.
        backtrack("", numbers, visited);
        // resultSet에 있는 소수들의 개수를 반환한다.
        return resultSet.size();
    }

    public static void main(String[] args) {
        Solution sol = new Solution();
        // "17"로 만들 수 있는 소수의 개수를 출력한다. (예상 출력: 3)
        System.out.println(sol.solution("17")); // {7, 17, 71}

        sol.resultSet.clear(); // 결과셋 초기화

        // "011"로 만들 수 있는 소수의 개수를 출력한다. (예상 출력: 2)
        System.out.println(sol.solution("011")); // {1, 11}
    }
}