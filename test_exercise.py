"""
Day 02 실습 테스트

이 파일은 수정하지 마세요.
exercise.py의 함수들이 올바르게 구현되었는지 테스트합니다.
"""

import pytest
import os
import json
import tempfile
import shutil
from exercise import (
    read_text_file,
    write_text_file,
    read_csv_as_dicts,
    write_dicts_to_csv,
    read_json_file,
    write_json_file,
    csv_to_json,
    json_to_csv,
    filter_by_condition,
    group_and_count,
    calculate_statistics,
    simple_etl
)


@pytest.fixture
def temp_dir():
    """임시 디렉토리 생성 및 정리"""
    temp_path = tempfile.mkdtemp()
    yield temp_path
    shutil.rmtree(temp_path)


# =============================================================================
# Part 1: 파일 I/O 테스트
# =============================================================================

class TestReadTextFile:
    def test_read_simple_text(self, temp_dir):
        file_path = os.path.join(temp_dir, 'test.txt')
        with open(file_path, 'w', encoding='utf-8') as f:
            f.write('Hello, World!')

        result = read_text_file(file_path)
        assert result == 'Hello, World!'

    def test_read_korean_text(self, temp_dir):
        file_path = os.path.join(temp_dir, 'korean.txt')
        with open(file_path, 'w', encoding='utf-8') as f:
            f.write('안녕하세요')

        result = read_text_file(file_path)
        assert result == '안녕하세요'

    def test_read_multiline_text(self, temp_dir):
        file_path = os.path.join(temp_dir, 'multi.txt')
        content = "Line 1\nLine 2\nLine 3"
        with open(file_path, 'w', encoding='utf-8') as f:
            f.write(content)

        result = read_text_file(file_path)
        assert result == content


class TestWriteTextFile:
    def test_write_simple_text(self, temp_dir):
        file_path = os.path.join(temp_dir, 'output.txt')
        result = write_text_file(file_path, 'Hello')

        assert result == 5
        with open(file_path, 'r', encoding='utf-8') as f:
            assert f.read() == 'Hello'

    def test_write_korean_text(self, temp_dir):
        file_path = os.path.join(temp_dir, 'korean.txt')
        result = write_text_file(file_path, '안녕하세요')

        assert result == 5
        with open(file_path, 'r', encoding='utf-8') as f:
            assert f.read() == '안녕하세요'


class TestReadCsvAsDicts:
    def test_read_csv(self, temp_dir):
        file_path = os.path.join(temp_dir, 'test.csv')
        with open(file_path, 'w', encoding='utf-8') as f:
            f.write('name,age,city\n')
            f.write('홍길동,30,서울\n')
            f.write('김영희,25,부산\n')

        result = read_csv_as_dicts(file_path)

        assert len(result) == 2
        assert result[0]['name'] == '홍길동'
        assert result[0]['age'] == '30'
        assert result[1]['city'] == '부산'

    def test_read_empty_csv(self, temp_dir):
        file_path = os.path.join(temp_dir, 'empty.csv')
        with open(file_path, 'w', encoding='utf-8') as f:
            f.write('name,age\n')

        result = read_csv_as_dicts(file_path)
        assert result == []


class TestWriteDictsToCsv:
    def test_write_csv(self, temp_dir):
        file_path = os.path.join(temp_dir, 'output.csv')
        data = [
            {'name': '홍길동', 'age': '30'},
            {'name': '김영희', 'age': '25'}
        ]
        fieldnames = ['name', 'age']

        result = write_dicts_to_csv(file_path, data, fieldnames)

        assert result == 2
        with open(file_path, 'r', encoding='utf-8') as f:
            lines = f.readlines()
            assert len(lines) == 3  # 헤더 + 2개 데이터


class TestReadJsonFile:
    def test_read_json_dict(self, temp_dir):
        file_path = os.path.join(temp_dir, 'test.json')
        data = {'name': '홍길동', 'age': 30}
        with open(file_path, 'w', encoding='utf-8') as f:
            json.dump(data, f, ensure_ascii=False)

        result = read_json_file(file_path)
        assert result == data

    def test_read_json_list(self, temp_dir):
        file_path = os.path.join(temp_dir, 'test.json')
        data = [{'name': '홍길동'}, {'name': '김영희'}]
        with open(file_path, 'w', encoding='utf-8') as f:
            json.dump(data, f, ensure_ascii=False)

        result = read_json_file(file_path)
        assert result == data


class TestWriteJsonFile:
    def test_write_json(self, temp_dir):
        file_path = os.path.join(temp_dir, 'output.json')
        data = {'name': '홍길동', 'age': 30}

        write_json_file(file_path, data)

        with open(file_path, 'r', encoding='utf-8') as f:
            result = json.load(f)
            assert result == data

    def test_write_json_korean(self, temp_dir):
        file_path = os.path.join(temp_dir, 'korean.json')
        data = {'이름': '홍길동'}

        write_json_file(file_path, data)

        with open(file_path, 'r', encoding='utf-8') as f:
            content = f.read()
            assert '홍길동' in content  # 한글이 이스케이프되지 않음


# =============================================================================
# Part 2: 데이터 변환 테스트
# =============================================================================

class TestCsvToJson:
    def test_convert(self, temp_dir):
        csv_path = os.path.join(temp_dir, 'input.csv')
        json_path = os.path.join(temp_dir, 'output.json')

        with open(csv_path, 'w', encoding='utf-8') as f:
            f.write('name,age\n')
            f.write('홍길동,30\n')
            f.write('김영희,25\n')

        result = csv_to_json(csv_path, json_path)

        assert result == 2
        with open(json_path, 'r', encoding='utf-8') as f:
            data = json.load(f)
            assert len(data) == 2


class TestJsonToCsv:
    def test_convert(self, temp_dir):
        json_path = os.path.join(temp_dir, 'input.json')
        csv_path = os.path.join(temp_dir, 'output.csv')

        data = [{'name': '홍길동', 'age': '30'}, {'name': '김영희', 'age': '25'}]
        with open(json_path, 'w', encoding='utf-8') as f:
            json.dump(data, f, ensure_ascii=False)

        result = json_to_csv(json_path, csv_path)

        assert result == 2


# =============================================================================
# Part 3: 데이터 처리 테스트
# =============================================================================

class TestFilterByCondition:
    def test_filter_match(self):
        data = [
            {'name': '홍길동', 'city': '서울'},
            {'name': '김영희', 'city': '부산'},
            {'name': '이철수', 'city': '서울'}
        ]
        result = filter_by_condition(data, 'city', '서울')

        assert len(result) == 2
        assert all(item['city'] == '서울' for item in result)

    def test_filter_no_match(self):
        data = [{'city': '서울'}, {'city': '부산'}]
        result = filter_by_condition(data, 'city', '대전')

        assert result == []

    def test_filter_empty_data(self):
        result = filter_by_condition([], 'city', '서울')
        assert result == []


class TestGroupAndCount:
    def test_group_count(self):
        data = [
            {'city': '서울'},
            {'city': '부산'},
            {'city': '서울'},
            {'city': '서울'},
            {'city': '부산'}
        ]
        result = group_and_count(data, 'city')

        assert result['서울'] == 3
        assert result['부산'] == 2

    def test_group_single_value(self):
        data = [{'city': '서울'}, {'city': '서울'}]
        result = group_and_count(data, 'city')

        assert result == {'서울': 2}

    def test_group_empty(self):
        result = group_and_count([], 'city')
        assert result == {}


class TestCalculateStatistics:
    def test_basic_statistics(self):
        result = calculate_statistics([1, 2, 3, 4, 5])

        assert result['sum'] == 15.0
        assert result['mean'] == 3.0
        assert result['min'] == 1.0
        assert result['max'] == 5.0

    def test_single_value(self):
        result = calculate_statistics([10])

        assert result['sum'] == 10.0
        assert result['mean'] == 10.0
        assert result['min'] == 10.0
        assert result['max'] == 10.0

    def test_negative_values(self):
        result = calculate_statistics([-5, 0, 5])

        assert result['sum'] == 0.0
        assert result['mean'] == 0.0
        assert result['min'] == -5.0
        assert result['max'] == 5.0


# =============================================================================
# Part 4: ETL 테스트
# =============================================================================

class TestSimpleEtl:
    def test_etl_without_filter(self, temp_dir):
        input_csv = os.path.join(temp_dir, 'input.csv')
        output_json = os.path.join(temp_dir, 'output.json')

        with open(input_csv, 'w', encoding='utf-8') as f:
            f.write('name,city\n')
            f.write('홍길동,서울\n')
            f.write('김영희,부산\n')

        result = simple_etl(input_csv, output_json)

        assert result['input_count'] == 2
        assert result['output_count'] == 2
        assert result['filtered'] == False

    def test_etl_with_filter(self, temp_dir):
        input_csv = os.path.join(temp_dir, 'input.csv')
        output_json = os.path.join(temp_dir, 'output.json')

        with open(input_csv, 'w', encoding='utf-8') as f:
            f.write('name,city\n')
            f.write('홍길동,서울\n')
            f.write('김영희,부산\n')
            f.write('이철수,서울\n')

        result = simple_etl(input_csv, output_json, filter_key='city', filter_value='서울')

        assert result['input_count'] == 3
        assert result['output_count'] == 2
        assert result['filtered'] == True

        with open(output_json, 'r', encoding='utf-8') as f:
            data = json.load(f)
            assert len(data) == 2
            assert all(item['city'] == '서울' for item in data)
