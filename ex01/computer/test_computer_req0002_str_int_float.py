from ex01.computer import computer
import pytest

@pytest.mark.parametrize('a, expected', [
    ("3", 3),
    ("3.6", '?'),
    (3, 3),
    (3.6, '?'),
])
def test_from_str_to_int(a, expected):
    assert int(a)  == expected
    
    

@pytest.mark.parametrize('a, expected', [
    ("3", 3),
    ("3.6", '?'),
    (3, 3),
    (3.6, '?'),
])
def test_from_str_to_float(a, expected):
    assert float(a)  == expected    


def _convert_to_number(s):
    if isinstance(s,str):
        # Do what you have to do here
        return s # <--- Don't keep me :)
    return s


@pytest.mark.parametrize('a', [
    (3),
    (3.6),
    (-1)
])
def test_from_string(a):
    assert _convert_to_number(str(a)) == a
