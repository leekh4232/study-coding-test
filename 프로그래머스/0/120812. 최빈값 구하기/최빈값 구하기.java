class Solution {
    public int solution(int[] array) {
        if (array.length == 0) {
            return -1;
        }

        // 고유 숫자와 빈도를 저장할 배열
        int[] uniqueNums = new int[array.length];
        int[] frequencies = new int[array.length];
        int uniqueCount = 0;

        // 배열을 순회하며 빈도를 계산
        for (int num : array) {
            boolean found = false;
            for (int i = 0; i < uniqueCount; i++) {
                if (uniqueNums[i] == num) {
                    frequencies[i]++;
                    found = true;
                    break;
                }
            }
            if (!found) {
                uniqueNums[uniqueCount] = num;
                frequencies[uniqueCount] = 1;
                uniqueCount++;
            }
        }

        // 최대 빈도 및 최빈값 찾기
        int maxFreq = 0;
        int mode = -1;
        boolean isUnique = true;

        for (int i = 0; i < uniqueCount; i++) {
            if (frequencies[i] > maxFreq) {
                maxFreq = frequencies[i];
                mode = uniqueNums[i];
                isUnique = true;
            } else if (frequencies[i] == maxFreq) {
                isUnique = false;
            }
        }

        if (isUnique) {
            return mode;
        }
        return -1;
    }
}