""" Write a function named frequency_dictionary that takes a list of elements named words as a parameter. The function should return a dictionary containing the frequency of each element in words. """

# Write your frequency_dictionary function here:
def frequency_dictionary(words):
  dicta = {}
  for key in words:
    if key not in dicta:
      dicta[key] = 0
    dicta[key] += 1
  return dicta


# Uncomment these function calls to test your  function:
print(frequency_dictionary(["apple", "apple", "cat", 1]))
# should print {"apple":2, "cat":1, 1:1}
print(frequency_dictionary([0,0,0,0,0]))
# should print {0:5}