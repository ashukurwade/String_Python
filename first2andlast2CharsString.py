def string_both_ends(str):
      if len(str) < 2:
          return ''
      
      return str[0:2] + str[-2:]

print(string_both_ends('Ashutosh'))
print(string_both_ends('As'))
print(string_both_ends('A'))