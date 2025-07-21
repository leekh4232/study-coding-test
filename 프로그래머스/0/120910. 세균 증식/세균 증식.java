class Solution {
    public int solution(int n, int t) {
        int t_pow = 1;
        
        for (int i=1; i<=t; i++) {
            t_pow *= 2;
        }
        
        return n * t_pow;
    }
}