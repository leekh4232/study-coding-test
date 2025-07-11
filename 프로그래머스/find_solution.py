

import os

def find_solution_code(root_path, problem_number, language):
    """
    지정된 루트 경로에서 문제 번호와 언어에 해당하는 코딩 테스트 풀이 파일을 찾아 코드를 반환합니다.

    Args:
        root_path (str): 검색을 시작할 최상위 디렉토리 경로입니다.
        problem_number (str): 찾고자 하는 문제의 번호입니다.
        language (str): 프로그래밍 언어입니다. (e.g., 'python', 'javascript', 'java', 'sql', 'go')

    Returns:
        str: 찾은 파일의 소스 코드 내용.

    Raises:
        ValueError: 지원하지 않는 언어일 경우 발생합니다.
    """
    lang_extensions = {
        'python': '.py',
        'javascript': '.js',
        'java': '.java',
        'sql': '.sql',
        'go': '.go'
    }

    target_extension = lang_extensions.get(language.lower())

    if not target_extension:
        raise ValueError(f"지원하지 않는 언어 '{language}'입니다. 지원 언어: {list(lang_extensions.keys())}")

    for dirpath, dirnames, filenames in os.walk(root_path):
        normalized_dirpath = dirpath.replace('\\', '/')
        #print(f"탐색 중: {normalized_dirpath}")
        if f'/{problem_number}.' in normalized_dirpath:
            for filename in filenames:
                if filename.endswith(target_extension):
                    file_path = os.path.join(dirpath, filename)
                    try:
                        with open(file_path, 'r', encoding='utf-8') as f:
                            print(f"--- 문제 {problem_number} ({language}) 풀이를 찾았습니다 ---")
                            print(f"파일 경로: {file_path}\n")
                            return f.read()
                    except Exception as e:
                        # 파일 읽기 오류 시 예외를 다시 발생시켜 호출자에게 알립니다.
                        raise IOError(f"파일을 읽는 중 오류가 발생했습니다: {file_path}") from e

    raise FileNotFoundError(f"해당 조건에 맞는 풀이 파일을 찾을 수 없습니다: 문제 번호 '{problem_number}', 언어 '{language}'")

if __name__ == '__main__':
    base_search_path = 'E:\\study-coding-test\\프로그래머스'

    try:
        problem_num_input = input("문제 번호를 입력하세요: ")
        language_input = input("언어를 입력하세요 (python, javascript, java, sql, go): ")
        print("\n" + "="*50 + "\n")

        solution_code = find_solution_code(base_search_path, problem_num_input, language_input)
        print(solution_code)

    except (FileNotFoundError, ValueError, IOError) as e:
        print(f"오류: {e}")
    except KeyboardInterrupt:
        print("\n사용자에 의해 작업이 중단되었습니다.")
