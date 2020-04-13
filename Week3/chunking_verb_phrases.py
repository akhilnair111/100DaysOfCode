from nltk import RegexpParser
from pos_tagged_oz import pos_tagged_oz
from vp_chunk_counter import vp_chunk_counter

# define verb phrase chunk grammar here
chunk_grammar = "VP: {<DT>?<JJ>*<NN><VB.*><RB.?>?}"

# create RegexpParser object here
chunk_parser = RegexpParser(chunk_grammar)

# create a list to hold verb-phrase chunked sentences
vp_chunked_oz = list()

# create for loop through each pos-tagged sentence in pos_tagged_oz here
for word in pos_tagged_oz:
  # chunk each sentence and append to vp_chunked_oz here
  vp_chunked_oz.append(chunk_parser.parse(word))
  
# store and print the most common vp-chunks here
most_common_vp_chunks = vp_chunk_counter(vp_chunked_oz)
