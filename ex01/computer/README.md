# EX01

## Object

We create a general computer for python user.

This computer does simple operations as addition, subsraction, multiplication and division.

Our computer is nevertheless special: it can succeed for several type of operand.

Are accepted as operand

* int, float
* string under condition
* list under condition
* tuple
* dict

## Requirements

### REQ001: operation with standard numbers

<a href="{{req001}}">go_to</a>

An operation with all accepted operators and standard python number as operand 
**must** return the standard result as defined in the python manual.

Example:
* add(1, 2) => 3, 
* add(0.1, 0.2) => 0.3
* multiply(0.2, 10.0) => 2.0
* ...

### REQ002: operation with string operands

As long as a string could parsed as number, 
it could be accepted as a valid operand

Example:
* add("1",2) => 3 

### REQ003: Operation with lists of same length

When operands are both lists of valid operands with the same length, operation is performed
on a per position basis and return a list of the same length.

Example:
* add([1,10,100],[2,20,200]) ==> [3,30,300]

### REQ0004: Operation with lists of different length

When operands are both of different length, a `ValueError` is raised.

### REQ0005: Operation with list and a scalar

When one the operand is a list and the other is a scalar, then the operation is performed 
on each value as if another list filled with the scalar value is provided.

Example:

* add([1,2,3], 10) => [11,12,13]


### REQ006: Operation with tuples of same length

When operands are both tuple of valid operands with the same length, operation is performed
on a per position basis and return a tuple of the same length.

Example:
* add([1,10,100],[2,20,200]) ==> [3,30,300]


### REQ0007: Operation with tuples of different length

When operands are both of different length, a `ValueError` is raised.


### REQ0008: Operation with tuple and a scalar

When one the operand is a tuple and the other is a scalar, then the operation is performed 
on each value as if another tuple filled with the scalar value is provided.

Example:

* add([1,2,3], 10) => [11,12,13]
