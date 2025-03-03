def quick_sort(arr):
    if len(arr) <= 1:
        return arr

    pivot = arr[len(arr) // 2]  # 피벗 설정 (가운데 요소 선택)
    left = [x for x in arr if x + pivot > pivot + x]  # 피벗보다 앞에 와야 할 요소
    middle = [x for x in arr if x + pivot == pivot + x]  # 동일한 경우
    right = [x for x in arr if x + pivot < pivot + x]  # 피벗보다 뒤에 와야 할 요소

    return quick_sort(left) + middle + quick_sort(right)

def solution(numbers):
    # 숫자들을 문자열로 변환
    num_strs = list(map(str, numbers))
    
    # 커스텀 정렬 (퀵 정렬 적용)
    sorted_numbers = quick_sort(num_strs)
    
    # 정렬된 리스트를 이어붙여 최종 결과 생성
    result = "".join(sorted_numbers)
    
    # 결과가 "000" 같은 경우 "0" 반환
    return result if result[0] != "0" else "0"

# ✅ 예제 테스트 실행
print(solution([6, 10, 2]))  # 결과: "6210"
print(solution([3, 30, 34, 5, 9]))  # 결과: "9534330"
