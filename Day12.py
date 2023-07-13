# 11 December 22
# string methods in python
a="Luffy"
print(len(a))
# Immutable in nature 
# String methods are done by making copies of orginal

# Upper Case 
print(a.upper())
# Lower Case
print(a.lower())
# strips trailing characters
b="Zoro!!!!"
print(b.rstrip("!"))
# replaces all occurences
print(a.replace("Luffy","Dragon"))
# Split() -> coverts string to list with respect to spaces b/w elements
z="ZORO SABO ACE LUFFY"
print(z.split(" "))
# Capitilize() -> Capitalizes the first letter(only first to upper and all other to lowercase) (doesn't exist in Js)
blogHead="introduction to python programming"
print(blogHead.capitalize())
# Center() -> method aligns string to center depending on parameter passed
center="Welcome"
print(center.center(50))
# Count() -> counts number of appearances of passed parameter in a given str
print(a.count('Luffy'))
# endswith() -> checks wheter string ends with a given value and retunrs bool value
print(blogHead.endswith("programming"))
# can also check for a value by providing a start and ending index 
print(blogHead.endswith("to",4,10))
# find() -> searches first occurences of a value and returns index, if not found -1 is given as o/p
print(blogHead.find("is"))
# Index() -> similar to find but for absolute occurences raises error if not found
print(blogHead.index("is"))
# isalnum() -> returns true if string contains alphanumeric val
print(blogHead.isalnum())
# isalpha() -> only alphabets
print(blogHead.isalpha())
# islower() -> if all characters are in lower course then true
# isupper() -> if all characters are in upper course then true
# isprintable() -> true if character is printable then true , else false(eg. \n)
# isspace() -> true if whitespaces exist, else false
# istitle() -> true only if first letter of string is in uppercase
# startswith() -> opposite of endswith
# swapcase() -> swaps uppercase to lowercase and lowercase to uppercase
# title() -> converts passed parameter to a title {capitalizes first letters}









