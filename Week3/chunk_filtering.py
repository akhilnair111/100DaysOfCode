""" Another option you have to find chunks in your text is chunk filtering. Chunk filtering lets you define what parts of speech you do not want in a chunk and remove them.

A popular method for performing chunk filtering is to chunk an entire sentence together and then indicate which parts of speech are to be filtered out. If the filtered parts of speech are in the middle of a chunk, it will split the chunk into two separate chunks! The chunk grammar you can use to perform chunk filtering is given below:

chunk_grammar = """NP: {<.*>+}
                       }<VB.?|IN>+{"""
NP is the user-defined name of the chunk you are searching for. In this case NP stands for noun phrase
The brackets {} indicate what parts of speech you are chunking. <.*>+ matches every part of speech in the sentence
The inverted brackets }{ indicate which parts of speech you want to filter from the chunk. <VB.?|IN>+ will filter out any verbs or prepositions
Chunk filtering provides an alternate way for you to search through a text and find the chunks of information useful for your analysis! """

from nltk import RegexpParser, Tree
from pos_tagged_oz import pos_tagged_oz

# define chunk grammar to chunk an entire sentence together
grammar = "Chunk: {<.*>+}"

# create RegexpParser object
parser = RegexpParser(grammar)

# chunk the pos-tagged sentence at index 230 in pos_tagged_oz
chunked_dancers = parser.parse(pos_tagged_oz[230])
print(chunked_dancers)

# define noun phrase chunk grammar using chunk filtering here
chunk_grammar = """NP: {<.*>+}
                       }<VB.?|IN>+{"""


# create RegexpParser object here
chunk_parser = RegexpParser(chunk_grammar)

# chunk and filter the pos-tagged sentence at index 230 in pos_tagged_oz here
filtered_dancers = chunk_parser.parse(pos_tagged_oz[230])
print(filtered_dancers)


# pretty_print the chunked and filtered sentence here
Tree.fromstring(str(filtered_dancers)).pretty_print()