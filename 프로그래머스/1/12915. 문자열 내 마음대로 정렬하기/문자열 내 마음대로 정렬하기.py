def solution(strings, n):
    answer = sorted(strings, key=lambda x: (x[n], x))
    return answer

if __name__ == "__main__":
    # ["car", "bed", "sun"]
    print(solution(["sun", "bed", "car"], 1))

    # ["abcd", "abce", "cdx"]
    print(solution(["abce", "abcd", "cdx"], 2))