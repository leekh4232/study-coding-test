# 백트래킹을 통해 가능한 모든 단어 조합을 생성하는 함수
def backtracking(cnt, w, words, wordList):
    # 단어 길이가 5가 되면 종료 (더 이상 추가하지 않음)
    if cnt == 5:
        return

    # 모음 리스트를 하나씩 붙여가며 재귀적으로 단어 생성
    for i in range(len(words)):
        # 현재 단어에 문자 추가
        newWord = w + words[i]
        # 완성된 단어를 리스트에 추가
        wordList.append(newWord)
        # 다음 글자를 붙이기 위해 재귀 호출
        backtracking(cnt + 1, newWord, words, wordList)

# 주어진 단어가 사전에서 몇 번째인지 반환하는 함수
def solution(word):
    # 사용할 모음 리스트 정의
    words = 'AEIOU'
    # 단어 조합 결과를 저장할 리스트
    wordList = []
    # 백트래킹 시작: 빈 문자열에서 출발, 현재 길이 0
    backtracking(0, "", words, wordList)
    # word가 몇 번째 단어인지 반환 (1-based index)
    return wordList.index(word) + 1

# 테스트
print(solution("AAAAE"))    # 6
print(solution("AAAE"))     # 10
print(solution("I"))        # 1563
print(solution("EIO"))      # 1189