import java.util.*;
import java.util.regex.*;

public class Solution {
    public static String[] solution(String[] files) {
        List<String[]> splitFiles = new ArrayList<>();

        // 파일명을 HEAD, NUMBER, TAIL로 분리
        for (String file : files) {
            Matcher matcher = Pattern.compile("([a-zA-Z\\-\\. ]+)([0-9]+)(.*)").matcher(file);  
            if (matcher.matches()) {
                splitFiles.add(new String[]{matcher.group(1), matcher.group(2), matcher.group(3)});
            }
        }

        // 정렬: HEAD(소문자로 변환) → NUMBER(정수 변환)
        splitFiles.sort((a, b) -> {
            int headCompare = a[0].toLowerCase().compareTo(b[0].toLowerCase());
            if (headCompare != 0) return headCompare;  // HEAD 기준 정렬

            int numCompare = Integer.compare(Integer.parseInt(a[1]), Integer.parseInt(b[1]));
            if (numCompare != 0) return numCompare;  // NUMBER 기준 정렬

            return 0;  // 입력 순서 유지
        });

        // 정렬된 파일명을 다시 문자열로 조합
        String[] answer = new String[files.length];
        for (int i = 0; i < splitFiles.size(); i++) {
            answer[i] = splitFiles.get(i)[0] + splitFiles.get(i)[1] + splitFiles.get(i)[2];
        }

        return answer;
    }

    public static void main(String[] args) {
        // ✅ 예제 테스트 실행
        System.out.println(Arrays.toString(solution(new String[]{
            "img12.png", "img10.png", "img02.png", "img1.png", "IMG01.GIF", "img2.JPG"
        })));
        // 결과: ["img1.png", "IMG01.GIF", "img02.png", "img2.JPG", "img10.png", "img12.png"]

        System.out.println(Arrays.toString(solution(new String[]{
            "F-5 Freedom Fighter", "B-50 Superfortress", "A-10 Thunderbolt II", "F-14 Tomcat"
        })));
        // 결과: ["A-10 Thunderbolt II", "B-50 Superfortress", "F-5 Freedom Fighter", "F-14 Tomcat"]
    }
}
