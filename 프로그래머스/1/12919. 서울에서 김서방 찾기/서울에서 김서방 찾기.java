import java.util.Arrays;

class Solution {
    public String solution(String[] seoul) {
        String answer = String.format("김서방은 %d에 있다", 
                                      Arrays.asList(seoul).indexOf("Kim"));
        return answer;
    }
}