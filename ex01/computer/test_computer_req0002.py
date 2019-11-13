from ex01.computer import computer

def test_add_scalar_string():
    assert computer.add("1", "2") == 3

def test_add_scalar_mixed_string():
    assert computer.add("1", 2) == 3
    
def test_add_scalar_float_string():
    assert computer.add("1.2", "2.3") == 3.5    

def test_multiply_scalar_string():
    assert computer.multiply("1", "2") == 2
    
def test_multiply_scalar_float_string():
    assert computer.multiply("1.3", "2.2") == 2.86
    
def test_add_with_not_numeric_string():
    assert computer.add("foo","2") != 0
