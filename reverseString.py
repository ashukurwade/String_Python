# program to reverse a string

s = "i love programming"
words = s.split(' ')
string =[]
for word in words:
	string.insert(0, word)

print("Reversed String:", " ".join(string))
#print(" ".join(string))