class Solution {
    public int[] solution(int n) {
        int size = n % 2 == 0 ? n / 2 : n / 2 + 1;
        int[] arr = new int[size];
        
        // int cur = 1;
        // for (int i=0; i<arr.length; i++) {
        //     arr[i] = cur;
        //     cur += 2;
        // }
        
        int i = 0;
        int cur = 1;
        while (cur <= n) {
            arr[i++] = cur;
            cur += 2;
        }
        
        return arr;
    }
}