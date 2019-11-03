## Extension of scope

## New requirements

### REQ0100: operations with dictionaries

When operands are dictionaries with accepted values, operation 
is performed on a same key basis and return a dictionary 
with only the same keys and the operation result.


Example

* add({'a': 1, 'b': 2, 'c': 3}, {'b': 2, 'c': 3, 'd': 4}) => {'b': 4, 'c': 6}

### REQ0101: operation with a function

When the **second** operand is a function, the **first** operand is passed
 to the function and the result is used as a operand to perform operation.
 
Example

* add(1,fn) => add(1,fn(1)) 

### REQ0102: operation with list and a function

When the **second** operand is a function, **each** item of the **first** operand is passed
 to the function and the result is used as a operand to perform operation.
 
Example

* add([1,2,3],fn) => add([1,2,3],[fn(1), fn(2), fn(3)]) 