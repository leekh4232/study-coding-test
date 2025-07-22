public class Solution {

    public static long solution(String numbers) {
        String[] words = {
            "zero", "one", "two", "three", "four",
            "five", "six", "seven", "eight", "nine"
        };

        for (int i = 0; i < words.length; i++) {
            numbers = numbers.replace(words[i], String.valueOf(i));
        }

        return Long.parseLong(numbers);  // ← 변경: long 처리
    }

    public static void main(String[] args) {
        System.out.println(solution("onetwothreefourfivesixseveneightnine")); // 123456789
        System.out.println(solution("nineninenineninenine")); // 99999
        System.out.println(solution("nine" + "nine".repeat(10))); // 매우 큰 수
    }
}
