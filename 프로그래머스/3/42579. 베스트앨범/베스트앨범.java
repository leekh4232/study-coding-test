import java.util.*;

public class Solution {

    // 베스트 앨범에 들어갈 노래 고유번호 리스트를 반환하는 메서드
    public static List<Integer> solution(String[] genres, int[] plays) {
        // 최종 결과를 저장할 리스트
        List<Integer> answer = new ArrayList<>();

        // 장르별 총 재생수를 저장할 맵
        HashMap<String, Integer> genreTotal = new HashMap<>();

        // 장르별 (고유번호, 재생수) 리스트를 저장할 맵
        HashMap<String, List<int[]>> genreMap = new HashMap<>();

        // genres와 plays를 순회하며 맵 구성
        for (int i = 0; i < genres.length; i++) {
            String genre = genres[i];
            int play = plays[i];

            // 총 재생수 누적
            genreTotal.put(genre, genreTotal.getOrDefault(genre, 0) + play);

            // 고유번호와 재생수를 리스트에 추가
            genreMap.computeIfAbsent(genre, k -> new ArrayList<>()).add(new int[]{i, play});
        }

        // 장르를 총 재생수 기준으로 정렬
        List<String> sortedGenres = new ArrayList<>(genreTotal.keySet());
        sortedGenres.sort((g1, g2) -> genreTotal.get(g2) - genreTotal.get(g1));

        // 정렬된 장르 순서대로 곡 선택
        for (String genre : sortedGenres) {
            // 장르 내 곡들을 재생수 내림차순, 고유번호 오름차순으로 정렬
            List<int[]> songs = genreMap.get(genre);
            songs.sort((a, b) -> {
                if (b[1] == a[1]) return a[0] - b[0]; // 재생수 같으면 고유번호 오름차순
                return b[1] - a[1]; // 재생수 내림차순
            });

            // 상위 2곡까지 결과에 추가
            for (int i = 0; i < songs.size() && i < 2; i++) {
                answer.add(songs.get(i)[0]);
            }
        }

        // 최종 결과 반환
        return answer;
    }

    // 테스트 케이스 실행을 위한 main 메서드
    public static void main(String[] args) {
        String[] genres = {"classic", "pop", "classic", "classic", "pop"};
        int[] plays = {500, 600, 150, 800, 2500};

        // 결과 출력
        System.out.println(solution(genres, plays)); // [4, 1, 3, 0]
    }
}