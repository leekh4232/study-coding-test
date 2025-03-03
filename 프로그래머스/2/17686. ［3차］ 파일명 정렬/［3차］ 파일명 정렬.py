import re

def solution(files):
    split = []

    for f in files:
        split.append(re.split(r"([0-9]+)", f))

    sorted_files = sorted(split, key = lambda x: (x[0].lower(), int(x[1])))

    answer = []
    for s in sorted_files:
        answer.append("".join(s))

    return answer

if __name__ == "__main__":
    print(solution(["img12.png", "img10.png", "img02.png", "img1.png", "IMG01.GIF", "img2.JPG"]))
    print(solution(["F-5 Freedom Fighter", "B-50 Superfortress", "A-10 Thunderbolt II", "F-14 Tomcat"]))