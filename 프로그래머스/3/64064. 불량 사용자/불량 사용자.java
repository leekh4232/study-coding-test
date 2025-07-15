import java.util.*;

class Solution {
    // 최종적으로 찾아낸 불량 사용자 ID 조합들을 저장하는 Set이다.
    // 각 조합은 비트마스크(정수) 형태로 저장되어 중복을 자동으로 방지한다.
    Set<Integer> resultSet = new HashSet<>();
    // 전체 사용자 ID 목록을 저장하는 배열이다.
    String[] users;
    // 불량 사용자 ID 패턴 목록을 저장하는 배열이다.
    String[] banned;

    // solution 함수는 불량 사용자 ID 조합의 개수를 반환한다.
    public int solution(String[] user_id, String[] banned_id) {
        // 전역 변수에 user_id와 banned_id를 할당하여 dfs 함수에서 사용할 수 있도록 한다.
        users = user_id;
        banned = banned_id;
        // 깊이 우선 탐색(DFS)을 시작한다.
        // bannedIdx는 현재 처리해야 할 banned_id의 인덱스를, usedMask는 현재까지 선택된 user_id들의 비트마스크를 나타낸다.
        // 초기 호출은 첫 번째 banned_id (인덱스 0)부터 시작하며, 아직 사용된 user_id는 없으므로 usedMask는 0이다.
        dfs(0, 0);
        // 모든 가능한 조합을 탐색한 후, resultSet에 저장된 중복 없는 조합의 개수를 반환한다.
        return resultSet.size();
    }

    // dfs 함수는 불량 사용자 ID 조합을 재귀적으로 탐색한다.
    // bannedIdx: 현재 처리 중인 불량 사용자 ID 패턴의 인덱스
    // usedMask: 현재까지 선택된 사용자 ID들의 비트마스크
    void dfs(int bannedIdx, int usedMask) {
        // 모든 불량 사용자 ID 패턴에 대해 매칭되는 사용자 ID를 찾았다면,
        // 현재 usedMask는 유효한 조합이므로 resultSet에 추가하고 탐색을 종료한다.
        if (bannedIdx == banned.length) {
            resultSet.add(usedMask);
            return;
        }

        // 모든 user_id에 대해 반복한다.
        // i는 현재 user_id 배열의 인덱스를 나타낸다.
        for (int i = 0; i < users.length; i++) {
            // (usedMask & (1 << i)) != 0은 i번째 user_id가 이미 현재 조합에서 사용되었는지 확인한다.
            // 만약 이미 사용되었다면, 중복 사용을 피하기 위해 다음 user_id로 넘어간다.
            if ((usedMask & (1 << i)) != 0) {
                continue;
            }

            // 현재 user_id(users[i])가 현재 불량 사용자 ID 패턴(banned[bannedIdx])에 매치되는지 확인한다.
            if (matches(users[i], banned[bannedIdx])) {
                // 매치된다면, 다음 불량 사용자 ID 패턴을 처리하기 위해 재귀 호출한다.
                // bannedIdx를 1 증가시키고, 현재 user_id(i번째)를 usedMask에 추가하여 (1 << i)로 표시한다.
                dfs(bannedIdx + 1, usedMask | (1 << i));
            }
        }
    }

    // matches 함수는 주어진 userId가 bannedId 패턴에 매치되는지 확인한다.
    // userId: 실제 사용자 ID
    // bannedId: 불량 사용자 ID 패턴 (와일드카드 '*' 포함 가능)
    boolean matches(String userId, String bannedId) {
        // 두 문자열의 길이가 다르면 매치될 수 없다.
        if (userId.length() != bannedId.length()) {
            return false;
        }
        // 각 문자를 순회하며 매치 여부를 확인한다.
        for (int i = 0; i < userId.length(); i++) {
            // bannedId의 i번째 문자가 '*'이 아니고, userId의 i번째 문자와 bannedId의 i번째 문자가 다르면 매치되지 않는다.
            // '*'은 어떤 문자든 매치될 수 있다.
            if (bannedId.charAt(i) != '*' && userId.charAt(i) != bannedId.charAt(i)) {
                return false;
            }
        }
        // 모든 문자가 성공적으로 매치되거나 와일드카드 처리되었다면 true를 반환한다.
        return true;
    }
}