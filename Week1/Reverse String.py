# Write your reverse_string function here:
def reverse_string(word):
  reverse = ""
  for i in range(len(word)-1, -1, -1):
    reverse += word[i]
  return reverse

# Uncomment these function calls to test your  function:
print(reverse_string("Codecademy"))
# should print ymedacedoC
print(reverse_string("Hello world!"))
# should print !dlrow olleH
print(reverse_string(""))
# should print


---------------------------------------------------------------------------------------------------------

def reverse_string(word):
    rev_string = ""
    for i in word:
        rev_string = i + rev_string
    return rev_string