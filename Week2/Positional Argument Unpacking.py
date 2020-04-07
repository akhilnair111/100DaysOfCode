""" We don’t always know how many arguments a function is going to receive, and sometimes we want to handle any possibility that comes at us. Python gives us two methods of unpacking arguments provided to functions. The first method is called positional argument unpacking, because it unpacks arguments given by position. Here’s what that looks like:

def shout_strings(*args):
  for argument in args:
    print(argument.upper())

shout_strings("hi", "what do we have here", "cool, thanks!")
# Prints out:
# "HI"
# "WHAT DO WE HAVE HERE"
# "COOL, THANKS!"
In shout_strings() we use a single asterisk (*) to indicate we’ll accept any number of positional arguments passed to the function. Our parameter args is a tuple of all of the arguments passed. In this case args has three values inside, but it can have many more (or fewer).

Note that args is just a parameter name, and we aren’t limited to that name (although it is rather standard practice). We can also have other positional parameters before our *args parameter. We can’t, as we’ll see, :

def truncate_sentences(length, *sentences):
  for sentence in sentences:
    print(sentence[:length])

truncate_sentences(8, "What's going on here", "Looks like we've been cut off")
# Prints out:
# "What's g"
# "Looks li"
Above we defined a function truncate_sentences that takes a length parameter and also any number of sentences. The function prints out the first length many characters of each sentence in sentences.

Instructions
1.
The Python library os.path has a function called join(). join() takes an arbitrary number of paths as arguments.

Use the join() function to join all three of the path segments, and print out the results!

2.
Write your own function, called myjoin() which takes an arbitrary number of strings and appends them all together, similar to os.path.join(). """


from os.path import join

path_segment_1 = "/Home/User"
path_segment_2 = "Codecademy/videos"
path_segment_3 = "cat_videos/surprised_cat.mp4"

# join all three of the paths here!
print(join(path_segment_1, path_segment_2, path_segment_3))

def myjoin(*args):
  joined_string = args[0]
  for arg in args[1:]:
    joined_string += '/' + arg
  return joined_string

print(myjoin(path_segment_1, path_segment_2, path_segment_3))