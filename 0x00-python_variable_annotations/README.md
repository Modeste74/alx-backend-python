0x00. Python - Variable Annotations
Python
Back-end

Type annotations in Python 3 refer to the ability to declare the data types of variables and function parameters within your code. They are not mandatory for Python to execute, but they provide clarity about the expected types and aid in static analysis tools' work like mypy.

Using Type Annotations:
1. Variable Annotations:
You can annotate variables by declaring their types using a colon followed by the type. For instance:

x: int = 5
name: str = "Alice"

2. Function Signatures:
Type annotations can be used to specify the types of parameters and return values in functions:

def add_numbers(a: int, b: int) -> int:
    return a + b

Duck Typing:
Python is dynamically typed, meaning the type of an object is determined at runtime. Duck typing is a concept where the type or the class of an object is less important than the methods or properties it provides. For instance, if an object has a method quack(), in duck typing, it is considered a duck (metaphorically speaking, "if it looks like a duck and quacks like a duck, it must be a duck").
