""" Most of us have a good autocorrect story. Our phone’s messenger quietly swaps one letter for another as we type and suddenly the meaning of our message has changed (to our horror or pleasure). However, addressing text similarity — including spelling correction — is a major challenge within natural language processing.

Addressing word similarity and misspelling for spellcheck or autocorrect often involves considering the Levenshtein distance or minimal edit distance between two words. The distance is calculated through the minimum number of insertions, deletions, and substitutions that would need to occur for one word to become another. For example, turning “bees” into “beans” would require one substitution (“a” for “e”) and one insertion (“n”), so the Levenshtein distance would be two.

Phonetic similarity is also a major challenge within speech recognition. English-speaking humans can easily tell from context whether someone said “euthanasia” or “youth in Asia,” but it’s a far more challenging task for a machine! More advanced autocorrect and spelling correction technology additionally considers key distance on a keyboard and phonetic similarity (how much two words or phrases sound the same).

It’s also helpful to find out if texts are the same to guard against plagiarism, which we can identify through lexical similarity (the degree to which texts use the same vocabulary and phrases). Meanwhile, semantic similarity (the degree to which documents contain similar meaning or topics) is useful when you want to find (or recommend) an article or book similar to one you recently finished.

Instructions
1.
Assign the variable three_away_from_code a word with a Levenshtein distance of 3 from “code”. Assign two_away_from_chunk a word with a Levenshtein distance of 2 from “chunk”. """


import nltk
# NLTK has a built-in function
# to check Levenshtein distance:
from nltk.metrics import edit_distance

def print_levenshtein(string1, string2):
  print("The Levenshtein distance from '{0}' to '{1}' is {2}!".format(string1, string2, edit_distance(string1, string2)))

# Check the distance between
# any two words here!
print_levenshtein("fart", "target")

# Assign passing strings here:
three_away_from_code = "cloud"

two_away_from_chunk = "dunk"

print_levenshtein("code", three_away_from_code)
print_levenshtein("chunk", two_away_from_chunk)