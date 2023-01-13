# In Python, Updation or deletion of characters from a String is not allowed.
# This will cause an error because item assignment or item deletion from a String is not supported. 
# Although deletion of the entire String is possible with the use of a built-in del keyword.
# This is because Strings are immutable, hence elements of a String cannot be changed once it has been assigned.
# Only new strings can be reassigned to the same name.

String1 = "Hello I am a student"
print(String1)

# Updating a character of the String
# As python strings are immutable, they don't support item updation directly
# there are following two ways
#1
list1 = list(String1)
list1[2] = 'i'
String2 = ''.join(list1)
print("\nUpdating character at 2nd Index: ")
print(String2)
 
#2
String3 = String1[0:2] + 'i' + String1[3:]
print(String3)

# Python Program to Update entire String
 
String1 = "Hello, I'm a Programmer"
print("\nInitial String: ")
print(String1)
 
# Updating a String
String1 = "Welcome to Programming"
print("\nUpdated String: ")
print(String1)


# Python Program to Delete characters from a String
 
String1 = "Hello, I'm Ashutosh"
print("Initial String: ")
print(String1)
 
# Deleting a character of the String
String2 = String1[0:2] + String1[3:]
print("\nDeleting character at 2nd Index: ")
print(String2)

# Python Program to Delete entire String
 
String1 = "Hello, I'm a Student"
print("\nInitial String: ")
print(String1)
 
# Deleting a String with the use of del
del String1
print("\nDeleting entire String: ")
print(String1)