from ex01.computer import computer

"""
Code the computer module's function `add` and `multiply` following these usecases 
"""

# REQ001: operation with standard numbers

def test_add_int():
    assert computer.add(1, 2) == 3
    
def test_add_float():
    assert computer.add(1.2, 2.3) == 3.5    

def test_substract_int():
    assert computer.substract(3, 2) == 1
    
def test_substract_float():
    assert computer.add(2.3, 1.2) == 1.1    


@pytest.mark.parametrize('operation, a, b, expected',[
    ('__add__', 1, 1, 2),
    ('__sub__', 1, 1, 0),
])
def test__call_operator(operation, a, b, expected):
    assert computer._call_operator(operation,a,b) == expected
