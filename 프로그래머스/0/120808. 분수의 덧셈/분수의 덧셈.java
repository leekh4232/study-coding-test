class Solution {
    public int[] solution(int numer1, int denom1, int numer2, int denom2) {
        int[] answer = new int[2];
    
        int numer3 = denom2 * numer1 + numer2 * denom1;
        int denom3 = denom1 * denom2;

        int i = numer3;

        for (; i > 0; i--) {
            if (numer3 % i == 0 && denom3 % i == 0) {
                break;
            }
        }

        answer[0] = numer3 / i;
        answer[1] = denom3 / i;
        
        return answer;
    }
}