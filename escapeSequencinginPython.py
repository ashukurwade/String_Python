# Escape sequences start with a backslash and can be interpreted differently
# If single quotes are used to represent a string,
# then all the single quotes present in the string must be escaped and
# same is done for Double Quotes.

# Python Program for Escape Sequencing of String
 
# Initial String
String1 = '''I'm a "Shark"'''
print("Initial String with use of Triple Quotes: ")
print(String1)

# Escaping Single Quote
String1 = 'I\'m a "Shark"'
print("\nEscaping Single Quote: ")
print(String1)

# Escaping Double Quotes
String1 = "I'm a \"Shark\""
print("\nEscaping Double Quotes: ")
print(String1)
 
# Printing Paths with the use of Escape Sequences
String1 = "C:\\Python\\Programs\\"
print("\nEscaping Backslashes: ")
print(String1)

# Printing Paths with the use of Tab
String1 = "Hi\tSharks"
print("\nTab: ")
print(String1)
 
# Printing Paths with the use of New Line
String1 = "Python\nPrograms"
print("\nNew Line: ")
print(String1)