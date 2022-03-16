"""
Correct variable names consist only of English letters, digits and underscores and they can't start with a digit.

Check if the given string is a correct variable name.

Example

For name = "var_1__Int", the output should be
solution(name) = true;
For name = "qq-q", the output should be
solution(name) = false;
For name = "2w2", the output should be
solution(name) = false.
"""
def solution(name):
    return name.isidentifier()
  
"""
In Python 3 you can use str.isidentifier() to test whether a given string is a valid Python identifier/name.

>>> 'X'.isidentifier()
True
>>> 'X123'.isidentifier()
True
>>> '2'.isidentifier()
False
>>> 'while'.isidentifier()
True
The last example shows that you should also check whether the variable name clashes with a Python keyword:

>>> from keyword import iskeyword
>>> iskeyword('X')
False
>>> iskeyword('while')
True
So you could put that together in a function:

from keyword import iskeyword

def is_valid_variable_name(name):
    return name.isidentifier() and not iskeyword(name)
"""
