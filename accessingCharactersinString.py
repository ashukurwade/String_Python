# Accessing characters in Python String
# In Python, individual characters of a String can be accessed by using the method of Indexing.
# Indexing allows negative address references to access characters from the back of the String
# e.g. -1 refers to the last character, -2 refers to the second last character, and so on.

# While accessing an index out of the range will cause an IndexError.
# Only Integers are allowed to be passed as an index, float or other types that will cause a TypeError.


string1 = (" Ashutosh ")
print(string1)

print(string1[5])

print(string1[-2])

print(string1[2])