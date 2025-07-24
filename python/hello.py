arr = [1, 2, 3]
n = len(arr)

for i in range(1 << n):  # 0부터 2^n - 1까지
    subset = []

    for j in range(n):
        if i & (1 << j):  # j번째 비트가 켜져 있는가?
            subset.append(arr[j])

    print(subset)
