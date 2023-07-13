# Docstrings & pep-8

# docstrings are the string literals that appear after defination of a function method or class or modules
# docstrings are written above definition, above declaration
def square(n):
    '''Takes a number n , returns the square of n''' #dis a docstring
    print(n**2)
square(5)
print(square.__doc__) #unlike comments these are special string, these have an effect on program unlike comments

# Pep-8 is a guideline for python for consistency (Python Enhancement Proposal)
# Beautiful is better than ugly.
# Explicit is better than implicit.
# Simple is better than complex.
# Complex is better than complicated.
# Flat is better than nested.
# Sparse is better than dense.
# Readability counts.
# Special cases aren't special enough to break the rules.
# Although practicality beats purity.
# Errors should never pass silently.
# Unless explicitly silenced.
# In the face of ambiguity, refuse the temptation to guess.
# There should be one-- and preferably only one --obvious way to do it.
# Although that way may not be obvious at first unless you're Dutch.
# Now is better than never.
# Although never is often better than *right* now.
# If the implementation is hard to explain, it's a bad idea.
# If the implementation is easy to explain, it may be a good idea.
# Namespaces are one honking great idea -- let's do more of those!
