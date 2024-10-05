import hashlib
import os
import subprocess
import pytest

def run_script_and_check(file_path, expected_hash, test_type):
    result = subprocess.run(['python', file_path], text=True, stdout=subprocess.PIPE, stderr=subprocess.PIPE, encoding='utf-8')
    output_hash = hashlib.md5(result.stdout.strip().encode()).hexdigest()
    assert output_hash == expected_hash, f"{test_type}: Script failed to run successfully"

class TestScripts:
    test_cases = [
        (1, '735b90b4568125ed6c3f678819b6e058', 'TestType_1'),
        (10, 'aab3238922bcc25a6f606eb525ffdc56', 'TestType_1'),
        (2, 'e0abee87e4ba1de22c6b8cf076c5016b', 'TestType_2'),
        (11, '7379de4777f5748aa568b8d0bf8c3795', 'TestType_2'),
        (3, '25f44e52e16f79a3cacc8fdd3c3abf29', 'TestType_3'),
        (12, 'c3a268e16fb2c7ae9f2c1ef90d42008f', 'TestType_3'),
        (4, 'c74d97b01eae257e44aa9d5bade97baf', 'TestType_4'),
        (13, '698d51a19d8a121ce581499d7b701668', 'TestType_4'),
        (5, '7f975a56c761db6506eca0b37ce6ec87', 'TestType_5'),
        (14, '1f0e3dad99908345f7439f8ffabdffc4', 'TestType_5'),
        (6, 'eecca5b6365d9607ee5a9d336962c534', 'TestType_6'),
        (15, '093f65e080a295f8076b1c5722a46aa2', 'TestType_6'),
        (7, 'ea5d2f1c4608232e07d3aa3d998e5135', 'TestType_7'),
        (16, 'e4da3b7fbbce2345d7772b0674a318d5', 'TestType_7'),
        (8, '5249ee8e0cff02ad6b4cc0ee0e50b7d1', 'TestType_8'),
        (17, 'd67d496249f30f93dd6a7a6d84701d60', 'TestType_8'),
        (9, '812b4ba287f5ee0bc9d43bbf5bbe87fb', 'TestType_9'),
        (18, '67388f1834f7d6243b753ec33584a8df', 'TestType_9')
    ]

    @pytest.mark.parametrize("file_index, expected_hash, test_type", test_cases)
    def test_scripts(self, file_index, expected_hash, test_type):
        file_path = f'../Тема {int(test_type.split("_")[1])}/Задания/Задание {file_index}.py'
        if not os.path.exists(file_path):
            pytest.skip(reason="Ещё не решено")
        else:
            run_script_and_check(file_path, expected_hash, test_type)