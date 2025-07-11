class Solution {
    public int solution(int[] array) {
        int n = array.length;
        
        for (int i=0; i<n-1; i++) {
            for (int j=i+1; j<n; j++) {
                if (array[i] > array[j]) {
                    int tmp = array[i];
                    array[i] = array[j];
                    array[j] = tmp;
                }
            }
        }
        
        return array[n / 2];
    }
}