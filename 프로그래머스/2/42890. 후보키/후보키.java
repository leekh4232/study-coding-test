import java.util.*;

class Solution {
    // solution 함수는 후보 키의 개수를 반환한다.
    public int solution(String[][] relation) {
        // 릴레이션의 행(튜플)의 개수를 저장한다.
        int rowCount = relation.length;
        // 릴레이션의 열(속성)의 개수를 저장한다.
        int colCount = relation[0].length;
        // 찾아낸 후보 키들을 저장할 리스트를 선언한다.
        // 각 후보 키는 비트마스크 형태로 저장된다.
        List<Integer> candidateKeys = new ArrayList<>();

        // 모든 가능한 속성 조합(부분집합)을 순회한다.
        // mask는 1부터 시작하여 모든 컬럼이 선택된 경우(1 << colCount) - 1까지 증가한다.
        // 예를 들어 colCount가 3이면 mask는 001(1)부터 111(7)까지 순회한다.
        for (int mask = 1; mask < (1 << colCount); mask++) {
            // 현재 mask가 이미 찾아낸 후보 키의 부분집합인지 확인한다.
            // 부분집합이라면 최소성을 만족하지 않으므로 다음 mask로 넘어간다.
            if (!isMinimal(mask, candidateKeys)) {
                continue;
            }

            // 현재 mask가 유일성 조건을 만족하는지 확인한다.
            if (isUnique(mask, rowCount, colCount, relation)) {
                // 유일성까지 만족한다면, 이 mask는 후보 키이므로 리스트에 추가한다.
                candidateKeys.add(mask);
            }
        }

        // 최종적으로 찾아낸 후보 키의 개수를 반환한다.
        return candidateKeys.size();
    }

    // isMinimal 함수는 현재 mask가 후보 키의 최소성을 만족하는지 검사한다.
    private boolean isMinimal(int mask, List<Integer> candidateKeys) {
        // 이미 찾아낸 각 후보 키(key)에 대해 반복한다.
        for (int key : candidateKeys) {
            // 현재 mask와 기존 후보 키 key를 비트 AND 연산했을 때 결과가 key와 같다면,
            // 이는 key가 mask의 부분집합이라는 의미이다.
            // 즉, mask는 key보다 더 많은 속성을 포함하면서도 key의 유일성을 이미 포함하고 있으므로,
            // mask는 최소성을 만족하지 않는다.
            if ((mask & key) == key) {
                return false;
            }
        }
        // 모든 기존 후보 키에 대해 부분집합이 아님이 확인되면 최소성을 만족한다.
        return true;
    }

    // isUnique 함수는 현재 mask가 후보 키의 유일성을 만족하는지 검사한다.
    private boolean isUnique(int mask, int rowCount, int colCount, String[][] relation) {
        // 현재 mask에 해당하는 속성들로 구성된 튜플들을 저장할 HashSet을 선언한다.
        // HashSet은 중복된 값을 허용하지 않으므로 유일성 검사에 적합하다.
        Set<String> uniqueTuples = new HashSet<>();
        // 각 행(튜플)에 대해 반복한다.
        for (int i = 0; i < rowCount; i++) {
            // 현재 튜플의 선택된 속성 값들을 조합하여 문자열을 만들기 위한 StringBuilder를 선언한다.
            StringBuilder sb = new StringBuilder();
            // 각 열(속성)에 대해 반복한다.
            for (int j = 0; j < colCount; j++) {
                // mask의 j번째 비트가 1인지 확인한다.
                // (mask >> j) & 1 이 1이면 j번째 속성이 선택된 것이다.
                if (((mask >> j) & 1) == 1) {
                    // 선택된 속성의 값을 StringBuilder에 추가하고, 구분자(콤마)를 붙인다.
                    sb.append(relation[i][j]).append(",");
                }
            }
            // 완성된 튜플 문자열을 uniqueTuples HashSet에 추가한다.
            uniqueTuples.add(sb.toString());
        }
        // HashSet의 크기가 전체 행의 개수(rowCount)와 같다면,
        // 모든 튜플이 유일하게 식별된다는 의미이므로 유일성을 만족한다.
        return uniqueTuples.size() == rowCount;
    }
}