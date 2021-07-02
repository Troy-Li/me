"""
Commenting skills:

TODO: above every line of code comment what you THINK the line below does.
TODO: execute that line and write what actually happened next to it.

See example for first print statement
"""
import platform

# I think this will print "hello! Let's get started" by calling the print function.
print("hello! Let's get started")  # it printed "hello! Let's get started"

# I think it will declare a variable called some_words 
# and it'ii put a list of stings into it
some_words = ['what', 'does', 'this', 'line', 'do', '?']

# I think it will find the word in some word 
for word in some_words:
    print(word)
# it will print the word
# it will  find the x in some_words
for x in some_words:
    print(x)
# it will print the x
# it will print some word
print(some_words)

if len(some_words) > 3:
    print('some_words contains more than 3 words')
#if the length of some_word is more than three, ptint some_words contains more than 3 words
def usefulFunction():
    """
    You may want to look up what uname does before you guess
    what the line below does:
    https://docs.python.org/3/library/platform.html#platform.uname
    """
    print(platform.uname())

usefulFunction()
