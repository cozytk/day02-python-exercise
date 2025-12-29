"""
Day 02 실습: Python 데이터 처리 기초

이 파일의 TODO 부분을 채워서 함수들을 완성하세요.
각 함수의 docstring에 힌트가 포함되어 있습니다.
테스트: docker-compose run --rm test
"""

import csv
import json
from typing import List, Dict, Any, Optional


# =============================================================================
# Part 1: 파일 I/O
# =============================================================================

def read_text_file(file_path: str) -> str:
    """
    텍스트 파일을 읽어 내용을 반환합니다.

    Args:
        file_path: 파일 경로

    Returns:
        str: 파일 내용

    Example:
        >>> read_text_file('sample.txt')
        'Hello, World!'

    힌트: with open(..., 'r', encoding='utf-8') as f: 를 사용하세요
    """
    # TODO: 여기에 코드를 작성하세요
    pass


def write_text_file(file_path: str, content: str) -> int:
    """
    텍스트 파일에 내용을 씁니다.

    Args:
        file_path: 파일 경로
        content: 저장할 내용

    Returns:
        int: 저장된 문자 수

    Example:
        >>> write_text_file('output.txt', 'Hello')
        5

    힌트: f.write()는 쓴 문자 수를 반환합니다
    """
    # TODO: 여기에 코드를 작성하세요
    pass


def read_csv_as_dicts(file_path: str) -> List[Dict[str, str]]:
    """
    CSV 파일을 읽어 딕셔너리 리스트로 반환합니다.

    Args:
        file_path: CSV 파일 경로

    Returns:
        List[Dict[str, str]]: 각 행이 딕셔너리인 리스트

    Example:
        # users.csv:
        # name,age,city
        # 홍길동,30,서울
        >>> read_csv_as_dicts('users.csv')
        [{'name': '홍길동', 'age': '30', 'city': '서울'}]

    힌트: csv.DictReader를 사용하세요
    """
    # TODO: 여기에 코드를 작성하세요
    pass


def write_dicts_to_csv(file_path: str, data: List[Dict], fieldnames: List[str]) -> int:
    """
    딕셔너리 리스트를 CSV 파일로 저장합니다.

    Args:
        file_path: 저장할 파일 경로
        data: 저장할 데이터 (딕셔너리 리스트)
        fieldnames: CSV 컬럼명 리스트

    Returns:
        int: 저장된 행 수 (헤더 제외)

    Example:
        >>> data = [{'name': '홍길동', 'age': 30}]
        >>> write_dicts_to_csv('output.csv', data, ['name', 'age'])
        1

    힌트: csv.DictWriter를 사용하세요. writeheader()와 writerows()를 활용하세요.
    """
    # TODO: 여기에 코드를 작성하세요
    pass


def read_json_file(file_path: str) -> Any:
    """
    JSON 파일을 읽어 Python 객체로 반환합니다.

    Args:
        file_path: JSON 파일 경로

    Returns:
        Any: 파싱된 JSON 데이터 (dict 또는 list)

    Example:
        >>> read_json_file('data.json')
        {'name': '홍길동', 'age': 30}

    힌트: json.load()를 사용하세요
    """
    # TODO: 여기에 코드를 작성하세요
    pass


def write_json_file(file_path: str, data: Any, indent: int = 2) -> None:
    """
    Python 객체를 JSON 파일로 저장합니다.

    Args:
        file_path: 저장할 파일 경로
        data: 저장할 데이터
        indent: 들여쓰기 (기본값: 2)

    힌트: json.dump()를 사용하세요. ensure_ascii=False 옵션으로 한글을 그대로 저장하세요.
    """
    # TODO: 여기에 코드를 작성하세요
    pass


# =============================================================================
# Part 2: 데이터 변환
# =============================================================================

def csv_to_json(csv_path: str, json_path: str) -> int:
    """
    CSV 파일을 JSON 파일로 변환합니다.

    Args:
        csv_path: 입력 CSV 파일 경로
        json_path: 출력 JSON 파일 경로

    Returns:
        int: 변환된 레코드 수

    힌트: 앞서 만든 read_csv_as_dicts()와 write_json_file()을 활용하세요
    """
    # TODO: 여기에 코드를 작성하세요
    pass


def json_to_csv(json_path: str, csv_path: str) -> int:
    """
    JSON 파일을 CSV 파일로 변환합니다.
    (JSON은 딕셔너리 리스트 형태라고 가정)

    Args:
        json_path: 입력 JSON 파일 경로
        csv_path: 출력 CSV 파일 경로

    Returns:
        int: 변환된 레코드 수

    힌트: 앞서 만든 read_json_file()과 write_dicts_to_csv()를 활용하세요
    """
    # TODO: 여기에 코드를 작성하세요
    pass


# =============================================================================
# Part 3: 데이터 처리 (Pandas 없이)
# =============================================================================

def filter_by_condition(data: List[Dict], key: str, value: Any) -> List[Dict]:
    """
    조건에 맞는 데이터만 필터링합니다.

    Args:
        data: 딕셔너리 리스트
        key: 필터링할 키
        value: 필터링할 값

    Returns:
        List[Dict]: 필터링된 데이터

    Example:
        >>> data = [{'name': '홍길동', 'city': '서울'}, {'name': '김영희', 'city': '부산'}]
        >>> filter_by_condition(data, 'city', '서울')
        [{'name': '홍길동', 'city': '서울'}]

    힌트: 리스트 컴프리헨션을 사용하면 간단합니다
    """
    # TODO: 여기에 코드를 작성하세요
    pass


def group_and_count(data: List[Dict], key: str) -> Dict[str, int]:
    """
    특정 키를 기준으로 그룹화하고 개수를 셉니다.

    Args:
        data: 딕셔너리 리스트
        key: 그룹화할 키

    Returns:
        Dict[str, int]: 그룹별 개수

    Example:
        >>> data = [{'city': '서울'}, {'city': '부산'}, {'city': '서울'}]
        >>> group_and_count(data, 'city')
        {'서울': 2, '부산': 1}

    힌트: 빈 딕셔너리를 만들고 for 루프로 카운트하거나,
          collections.Counter를 사용할 수 있습니다
    """
    # TODO: 여기에 코드를 작성하세요
    pass


def calculate_statistics(numbers: List[float]) -> Dict[str, float]:
    """
    숫자 리스트의 기본 통계를 계산합니다.

    Args:
        numbers: 숫자 리스트

    Returns:
        Dict[str, float]: {'sum': 합계, 'mean': 평균, 'min': 최소, 'max': 최대}

    Example:
        >>> calculate_statistics([1, 2, 3, 4, 5])
        {'sum': 15.0, 'mean': 3.0, 'min': 1.0, 'max': 5.0}

    힌트: sum(), min(), max(), len() 함수를 사용하세요
    """
    # TODO: 여기에 코드를 작성하세요
    pass


# =============================================================================
# Part 4: 간단한 ETL
# =============================================================================

def simple_etl(
    input_csv: str,
    output_json: str,
    filter_key: Optional[str] = None,
    filter_value: Optional[Any] = None
) -> Dict[str, Any]:
    """
    간단한 ETL 파이프라인을 수행합니다.

    Extract: CSV 파일 읽기
    Transform: (선택) 필터링
    Load: JSON 파일 저장

    Args:
        input_csv: 입력 CSV 파일 경로
        output_json: 출력 JSON 파일 경로
        filter_key: 필터링할 키 (None이면 필터링 안 함)
        filter_value: 필터링할 값

    Returns:
        Dict[str, Any]: {
            'input_count': 입력 레코드 수,
            'output_count': 출력 레코드 수,
            'filtered': 필터링 여부
        }

    힌트: 앞서 만든 함수들을 조합하세요
    """
    # TODO: 여기에 코드를 작성하세요
    pass
