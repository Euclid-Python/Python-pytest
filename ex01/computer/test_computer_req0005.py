from ex01.computer import computer
import pytest

def _as_list(s):
    # Do what you have to do here
    pass

@pytest.mark.parametrize('s, expected',[
    (3, [3]),
    ([1,2],[1,2])
])
def test_as_list(s, expected):
    assert _as_list(s) == expected

def _convert_as_list(*args):
    # Do here what you have to do.
    pass

@pytest.mark.parametrize('a, b, a_list, b_list',[
    (3,3,[3],[3]),
    (3,[1,2],[3],[1,2])
])
def test_as_list(a, b, a_list, b_list):
    assert _convert_as_list(a,b) == (a_list, b_list)

from ex01.computer import computer

def test_empty_5():
    assert False, 'No tests for REQ005'
