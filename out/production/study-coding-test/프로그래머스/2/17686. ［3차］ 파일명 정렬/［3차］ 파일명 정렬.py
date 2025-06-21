import re

def solution(files):
    split = []

    # 파일명을 HEAD, NUMBER, TAIL로 분리
    for f in files:
        split.append(re.split(r"([0-9]+)", f))  # 숫자를 기준으로 파일명을 분리

    # 정렬: HEAD(소문자로 변환) → NUMBER(정수 변환)
    sorted_files = sorted(split, key=lambda x: (x[0].lower(), int(x[1])))

    # 정렬된 파일명을 다시 문자열로 조합
    answer = []
    for s in sorted_files:
        answer.append("".join(s))  # 리스트를 다시 문자열로 합쳐 저장

    return answer

if __name__ == "__main__":
    # ✅ 예제 테스트 실행
    print(solution(["img12.png", "img10.png", "img02.png", "img1.png", "IMG01.GIF", "img2.JPG"]))
    # 결과: ["img1.png", "IMG01.GIF", "img02.png", "img2.JPG", "img10.png", "img12.png"]

    print(solution(["F-5 Freedom Fighter", "B-50 Superfortress", "A-10 Thunderbolt II", "F-14 Tomcat"]))
    # 결과: ["A-10 Thunderbolt II", "B-50 Superfortress", "F-5 Freedom Fighter", "F-14 Tomcat"]