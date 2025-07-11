import java.util.HashMap;
import java.util.Map;
import java.util.stream.IntStream;
import java.util.Arrays;

public class Solution {
    public int[] solution(String[] name, int[] yearning, String[][] photo) {
        Map<String, Integer> map = IntStream.range(0, name.length)
            .collect(HashMap::new, (m, i) -> m.put(name[i], yearning[i]), Map::putAll);

        return Arrays.stream(photo)
            .mapToInt(p -> Arrays.stream(p)
                                 .filter(map::containsKey)
                                 .mapToInt(map::get)
                                 .sum())
            .toArray();
    }
}