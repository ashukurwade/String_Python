#program to count number of substring of a string

def countNonEmptySubstr(str):
  n = len(str);
  return int (n*(n+1)/2);
s ='abcde'
print(countNonEmptySubstr(s));