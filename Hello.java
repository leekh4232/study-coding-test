List<Integer> result = new ArrayList<>();
Set<Integer> numberSet = new HashSet<>();

for (int num : numbers) { numberSet.add(num); }

for (int t : targets) {
    if (numberSet.contains(t)) { result.add(t); }
}