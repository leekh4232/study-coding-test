# 백트래킹을 통해 가능한 모든 단어 조합을 생성하는 함수이다.
# currentCount: 현재 단어의 길이를 나타낸다.
# currentWord: 현재까지 만들어진 단어를 문자열 형태로 저장한다.
# availableWords: 'A', 'E', 'I', 'O', 'U' 모음이 담긴 문자열이다.
# generatedWordList: 생성된 단어들을 저장할 리스트이다.
def backtracking(currentCount, currentWord, availableWords, generatedWordList):
    # 단어의 길이가 5가 되면 더 이상 문자를 추가하지 않고 종료한다.
    if currentCount == 5:
        return

    # 사용 가능한 각 모음에 대해 반복한다.
    for i in range(len(availableWords)):
        # 현재 단어(currentWord)에 모음(availableWords[i])을 추가하여 새로운 단어를 만든다.
        newWord = currentWord + availableWords[i]
        # 완성된 새로운 단어를 generatedWordList에 추가한다.
        generatedWordList.append(newWord)
        # 다음 글자를 붙이기 위해 currentCount를 1 증가시키고, newWord로 재귀 호출한다.
        backtracking(currentCount + 1, newWord, availableWords, generatedWordList)

# 주어진 단어가 사전에서 몇 번째인지 반환하는 함수이다.
def solution(word):
    # 사용할 모음들을 정의한다. (문자열 형태)
    availableWords = 'AEIOU'
    # 백트래킹을 통해 생성될 모든 단어들을 저장할 리스트를 초기화한다.
    generatedWordList = []
    # 백트래킹 프로세스를 시작한다.
    # 초기 단어 길이는 0이고, 시작 단어는 빈 문자열이다.
    backtracking(0, "", availableWords, generatedWordList)
    
    # generatedWordList에서 주어진 'word'의 인덱스를 찾아 반환한다.
    # 파이썬 리스트 인덱스는 0부터 시작하므로, 문제의 1-based 인덱스를 위해 1을 더해준다.
    return generatedWordList.index(word) + 1

# 직접 테스트를 위한 코드 블록이다.
if __name__ == "__main__":
    # "AAAAE"가 사전에서 몇 번째인지 출력한다. (예상 출력: 6)
    print(solution("AAAAE"))
    # "AAAE"가 사전에서 몇 번째인지 출력한다. (예상 출력: 10)
    print(solution("AAAE"))
    # "I"가 사전에서 몇 번째인지 출력한다. (예상 출력: 1563)
    print(solution("I"))
    # "EIO"가 사전에서 몇 번째인지 출력한다. (예상 출력: 1189)
    print(solution("EIO"))