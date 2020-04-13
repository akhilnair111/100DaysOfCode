import nltk
from nltk import pos_tag
from word_tokenized_oz import word_tokenized_oz

# save and print the sentence stored at index 100 in word_tokenized_oz here
witches_fate = word_tokenized_oz[100]
print(witches_fate)


# create a list to hold part-of-speech tagged sentences here
pos_tagged_oz = []

# create a for loop through each word tokenized sentence in word_tokenized_oz here
for word in word_tokenized_oz:
  pos_tagged_oz.append(pos_tag(word))
  # part-of-speech tag each sentence and append to pos_tagged_oz here
witches_fate_pos =  pos_tagged_oz[100] 

# store and print the 101st part-of-speech tagged sentence here
print(witches_fate_pos)
