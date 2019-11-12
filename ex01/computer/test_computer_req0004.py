from ex01.computer import computer
import pytest

def test_check_length_ok():
    assert computer._check_length([1,2],[1,2])
    

def test_check_length_ok():
    with pytest.raises(ValueError):
        assert computer._check_length([1,2],[1,2,3])

def test_empty_4():
    with pytest.raises(ValueError):
        assert computer.add([1,2],[1,2,3])
