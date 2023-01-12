# Reversing a Python String
# With Accessing Characters from a string, we can also reverse them.
# We can Reverse a string by writing [::-1] and the string will be reversed.

string1 = " Ashutosh "
print(string1)

print(string1[::-1])


# We can also reverse a string by using built-in join and reversed function.

string2 = " I completed daily course"

string2 = "".join(reversed(string2))
print(string2)