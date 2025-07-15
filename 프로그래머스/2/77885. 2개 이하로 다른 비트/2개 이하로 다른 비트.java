// https://school.programmers.co.kr/learn/courses/30/lessons/77885
class Solution {
    public long[] solution(long[] numbers) {
        // numbers 배열의 각 숫자에 대한 결과를 저장할 long 타입의 answer 배열을 선언한다.
        // answer 배열의 크기는 numbers 배열의 크기와 동일하다.
        long[] answer = new long[numbers.length];

        // numbers 배열의 각 숫자에 대해 반복한다.
        // i는 numbers 배열의 현재 인덱스를 나타낸다.
        for (int i = 0; i < numbers.length; i++) {
            // 현재 처리할 숫자를 num 변수에 저장한다.
            long num = numbers[i];

            // num이 짝수인지 홀수인지 확인한다.
            // num % 2 == 0은 num이 짝수임을 의미한다.
            if (num % 2 == 0) {
                // num이 짝수인 경우, 가장 오른쪽 비트가 0이다.
                // num보다 크고 비트가 1개만 다른 가장 작은 수는 num의 가장 오른쪽 0을 1로 바꾸는 것이다.
                // 이는 num에 1을 더하는 것과 동일하다.
                answer[i] = num + 1;
            } else {
                // num이 홀수인 경우, 가장 오른쪽 비트가 1이다.
                // num보다 크고 비트가 2개만 다른 가장 작은 수를 찾아야 한다.
                // 이는 num의 이진수에서 가장 오른쪽 0을 찾아 1로 바꾸고, 그 0의 바로 오른쪽 1을 0으로 바꾸는 것과 같다.

                // 비트 NOT 연산 (~num)은 num의 모든 비트를 반전시킨다.
                // -~num은 ~num의 2의 보수와 같다. 이는 ~num의 가장 오른쪽 1 비트만 1이고 나머지는 0인 값을 찾는다.
                // 이 두 값을 비트 AND 연산하면 num에서 가장 오른쪽에 있는 0 비트만 1이고 나머지는 0인 값을 얻을 수 있다.
                // 예를 들어, num이 7 (0...0111)일 때, ~num은 (1...1000)이 되고,
                // -~num은 (0...1000)이 된다 (부호 비트 고려).
                // (~num & -~num)은 (0...1000)이 된다. 이 값이 lowestZeroBit이다.
                long lowestZeroBit = ~num & -~num;

                // num에 lowestZeroBit를 더하면 가장 오른쪽 0이 1로 바뀐다.
                // lowestZeroBit를 2로 나누면 lowestZeroBit의 가장 오른쪽 1이 한 칸 오른쪽으로 쉬프트되어 0이 된다.
                // 예를 들어 lowestZeroBit가 8(1000)이면 lowestZeroBit / 2는 4(0100)이다.
                // 이는 원래 num에서 가장 오른쪽에 있던 1을 0으로 바꾸는 효과를 준다.
                // 따라서 num + lowestZeroBit + lowestZeroBit / 2를 하면
                // num에서 가장 오른쪽 0을 1로 바꾸고, 그 오른쪽에 있던 1을 0으로 바꾸는 결과가 된다.
                // 하지만 이 코드에서는 num + lowestZeroBit / 2를 한다.
                // 이는 num의 가장 오른쪽 0을 1로 만들고, 그 0의 오른쪽에 있는 모든 1들을 0으로 만드는 효과를 준다.
                // 예시: num = 7 (0...0111)
                // lowestZeroBit = 8 (0...1000)
                // answer[i] = 7 + 8 / 2 = 7 + 4 = 11 (0...1011)
                // 7 (0111) -> 11 (1011) (2개 비트 다름)
                answer[i] = num + lowestZeroBit / 2;
            }
        }
        // 모든 숫자에 대한 처리가 완료된 answer 배열을 반환한다.
        return answer;
    }
}