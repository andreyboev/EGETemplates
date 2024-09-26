import hashlib
import os
import subprocess
import pytest

file_paths = ['..\\Тема 1\\Задания\\Задание 1.py',
              '..\\Тема 2\\Задания\\Задание 2.py', '..\\Тема 3\\Задания\\Задание 3.py', '..\\Тема 4\\Задания\\Задание 4.py',
              '..\\Тема 5\\Задания\\Задание 5.py', '..\\Тема 6\\Задания\\Задание 6.py', '..\\Тема 7\\Задания\\Задание 7.py',
              '..\\Тема 8\\Задания\\Задание 8.py', '..\\Тема 9\\Задания\\Задание 9.py']
class TestType_1:
    @pytest.mark.skipif(not os.path.exists(file_paths[0]), reason="Ещё не решено")
    def test_1(self):
        result = subprocess.run(['python', file_paths[0]], text=True, stdout=subprocess.PIPE,
                                stderr=subprocess.PIPE)
        hash = hashlib.md5(result.stdout.strip().encode()).hexdigest()
        assert hash == '735b90b4568125ed6c3f678819b6e058', "Script failed to run successfully"

class TestType_2:
    @pytest.mark.skipif(not os.path.exists(file_paths[1]), reason="Ещё не решено")
    def test_2(self):
        result = subprocess.run(['python', file_paths[1]], text=True, stdout=subprocess.PIPE,
                                stderr=subprocess.PIPE)
        hash = hashlib.md5(result.stdout.strip().encode()).hexdigest()
        assert hash == 'e0abee87e4ba1de22c6b8cf076c5016b', "Script failed to run successfully"

class TestType_3:
    @pytest.mark.skipif(not os.path.exists(file_paths[2]), reason="Ещё не решено")
    def test_3(self):
        result = subprocess.run(['python', file_paths[2]], text=True, stdout=subprocess.PIPE,
                                stderr=subprocess.PIPE)
        hash = hashlib.md5(result.stdout.strip().encode()).hexdigest()
        assert hash == '25f44e52e16f79a3cacc8fdd3c3abf29', "Script failed to run successfully"

class TestType_4:
    @pytest.mark.skipif(not os.path.exists(file_paths[3]), reason="Ещё не решено")
    def test_4(self):
        result = subprocess.run(['python', file_paths[3]], text=True, stdout=subprocess.PIPE,
                                stderr=subprocess.PIPE)
        hash = hashlib.md5(result.stdout.strip().encode()).hexdigest()
        assert hash == 'c74d97b01eae257e44aa9d5bade97baf', "Script failed to run successfully"

class TestType_5:
    @pytest.mark.skipif(not os.path.exists(file_paths[4]), reason="Ещё не решено")
    def test_5(self):
        result = subprocess.run(['python', file_paths[4]], text=True, stdout=subprocess.PIPE,
                                stderr=subprocess.PIPE)
        hash = hashlib.md5(result.stdout.strip().encode()).hexdigest()
        assert hash == '7f975a56c761db6506eca0b37ce6ec87', "Script failed to run successfully"

class TestType_6:
    @pytest.mark.skipif(not os.path.exists(file_paths[5]), reason="Ещё не решено")
    def test_6(self):
        result = subprocess.run(['python', file_paths[5]], text=True, stdout=subprocess.PIPE,
                                stderr=subprocess.PIPE)
        hash = hashlib.md5(result.stdout.strip().encode()).hexdigest()
        assert hash == 'eecca5b6365d9607ee5a9d336962c534', "Script failed to run successfully"

class TestType_7:
    @pytest.mark.skipif(not os.path.exists(file_paths[6]), reason="Ещё не решено")
    def test_7(self):
        result = subprocess.run(['python', file_paths[6]], text=True, stdout=subprocess.PIPE,
                                stderr=subprocess.PIPE)
        hash = hashlib.md5(result.stdout.strip().encode()).hexdigest()
        assert hash == 'ea5d2f1c4608232e07d3aa3d998e5135', "Script failed to run successfully"

class TestType_8:
    @pytest.mark.skipif(not os.path.exists(file_paths[7]), reason="Ещё не решено")
    def test_8(self):
        result = subprocess.run(['python', file_paths[7]], text=True, stdout=subprocess.PIPE,
                                stderr=subprocess.PIPE)
        hash = hashlib.md5(result.stdout.strip().encode()).hexdigest()
        assert hash == '5249ee8e0cff02ad6b4cc0ee0e50b7d1', "Script failed to run successfully"

class TestType_9:
    @pytest.mark.skipif(not os.path.exists(file_paths[8]), reason="Ещё не решено")
    def test_9(self):
        result = subprocess.run(['python', file_paths[8]], text=True, stdout=subprocess.PIPE,
                                stderr=subprocess.PIPE)
        hash = hashlib.md5(result.stdout.strip().encode()).hexdigest()
        assert hash == '812b4ba287f5ee0bc9d43bbf5bbe87fb', "Script failed to run successfully"