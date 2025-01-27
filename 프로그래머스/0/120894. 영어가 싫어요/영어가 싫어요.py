def solution(numbers):
    words = ["zero", "one", "two", "three", "four", "five", "six", "seven", "eight", "nine"]
    
    for i, v in enumerate(words):
        numbers = numbers.replace(v, str(i))
    
    return int(numbers)