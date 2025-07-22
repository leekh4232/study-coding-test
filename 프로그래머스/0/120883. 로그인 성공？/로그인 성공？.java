public class Solution {

    public static String solution(String[] id_pw, String[][] db) {
        String answer = "fail"; // 기본값 설정

        for (int i = 0; i < db.length; i++) {
            String dbId = db[i][0];
            String dbPw = db[i][1];

            if (id_pw[0].equals(dbId)) {
                if (id_pw[1].equals(dbPw)) {
                    answer = "login";
                } else {
                    answer = "wrong pw";
                }
                break; // 아이디가 일치했으면 더 이상 반복할 필요 없음
            }
        }

        return answer;
    }

    // ✅ 테스트용 main 메서드
    public static void main(String[] args) {
        String[] id_pw1 = {"meosseugi", "1234"};
        String[][] db1 = {
            {"rardss", "123"},
            {"yyoom", "1234"},
            {"meosseugi", "1234"}
        };

        String[] id_pw2 = {"programmer01", "15789"};
        String[][] db2 = {
            {"programmer02", "111111"},
            {"programmer00", "134"},
            {"programmer01", "1145"}
        };

        String[] id_pw3 = {"rabbit04", "98761"};
        String[][] db3 = {
            {"jaja11", "98761"},
            {"krong0313", "29440"},
            {"rabbit00", "111333"}
        };

        System.out.println(solution(id_pw1, db1)); // login
        System.out.println(solution(id_pw2, db2)); // wrong pw
        System.out.println(solution(id_pw3, db3)); // fail
    }
}
