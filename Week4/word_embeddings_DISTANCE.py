''' Distance
The key at the heart of word embeddings is distance. Before we explain why, let’s dive into how the distance between vectors can be measured.

There are a variety of ways to find the distance between vectors, and here we will cover three. The first is called Manhattan distance.

In Manhattan distance, also known as city block distance, distance is defined as the sum of the differences across each individual dimension of the vectors. Consider the vectors [1,2,3] and [2,4,6]. We can calculate the Manhattan distance between them as shown below:

manhattan\ distance\ =\ \left | 1-2 \right |+\left | 2-4 \right| +\left | 3-6 \right|=1+2+3=6manhattan distance = ∣1−2∣+∣2−4∣+∣3−6∣=1+2+3=6
Another common distance metric is called the Euclidean distance, also known as straight line distance. With this distance metric, we take the square root of the sum of the squares of the differences in each dimension.

euclidean\ distance\ =\sqrt{(1-2)^{2})+(2-4)^{2})+(3-6)^{2})}=\sqrt{14}\approx 3.74euclidean distance = 
(1−2) 2)+(2−4) 2)+(3−6) 2) = sqrt14 ≈3.74
The final distance we will consider is the cosine distance. Cosine distance is concerned with the angle between two vectors, rather than by looking at the distance between the points, or ends, of the vectors. Two vectors that point in the same direction have no angle between them, and have a cosine distance of 0. Two vectors that point in opposite directions, on the other hand, have a cosine distance of 1. '''

import numpy as np
from scipy.spatial.distance import cityblock, euclidean, cosine
import spacy

# load word embedding model
nlp = spacy.load('en')

# define word embedding vectors
happy_vec = nlp('happy').vector
sad_vec = nlp('sad').vector
angry_vec = nlp('angry').vector

# calculate Manhattan distance
man_happy_sad = cityblock(happy_vec, sad_vec)
man_sad_angry = cityblock(sad_vec, angry_vec)
print(man_happy_sad)
print(man_sad_angry)

# calculate Euclidean distance
euc_happy_sad = euclidean(happy_vec, sad_vec)
euc_sad_angry = euclidean(sad_vec, angry_vec)
print(euc_happy_sad)
print(euc_sad_angry)
# calculate cosine distance
cos_happy_sad = cosine(happy_vec, sad_vec)
cos_sad_angry = cosine(sad_vec, angry_vec)
print(cos_happy_sad)
print(cos_sad_angry)

""" The cosine distance values, however, remain low and bounded between 0 and 1, where the Manhattan and Euclidean distances are rather large (and continue to grow as more dimensions are added to a vector). """


