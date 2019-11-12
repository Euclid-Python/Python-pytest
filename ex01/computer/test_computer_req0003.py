from ex01.computer import computer
import pytest

def _is_list(s):
    """Test if parameter is a list"""
    return isinstance(s,list)

def _are_all_iterable(*args):
    """Test if all arguments are list"""
    return all(is_list(arg) for arg in args)

def test_what_could_I_do_with_two_list():
    list0 = [1,2,3]
    list1 = [10,20,100]
    def proof_of_concept_of_ADD_with_two_lists(a,b):
        # Here your ideas
        #...
        pass
        
    assert proof_of_concept_of_ADD_with_two_lists(list0, list1) == [11,22,103]



def test_empty_3():
    assert False, 'No tests for REQ003'
