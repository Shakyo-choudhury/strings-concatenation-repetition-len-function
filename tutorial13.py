# strings in python
# immutable
# concatenation, slicing, and searching

# Single line string
str1 = 'Hello, World!'

# Single line string with double quotes
str2 = "Python is awesome!"

# Multiline string using triple quotes
str3 = '''This is a multiline string.
It can span multiple lines.
Python is versatile and powerful.'''


# concatenation
# var1 = "Hello "
# var2 = "Shakyo"


# # + Operator is used to combine strings
# var3 = var1 + var2
# print(var3)
var1 = "Shakyo"
var2 = "DC" 
 
# join() method is used to combine the strings
print("".join([var1, var2]))
 
# join() method is used here to combine
# the string with a separator Space(" ")
var3 = " ".join([var1, var2])
 
print(var3)

# *

str1="Hello"
print ("String 1:",str1)
str1=str1*3
print("Concatenated same string:",str1)

# length function
print(len('shakyo'))