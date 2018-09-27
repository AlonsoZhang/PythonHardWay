# 总结：
#
# class Tell Python to make a new type of thing.
# object Two meanings: the most basic type of thing, and any instance of some thing.
# instance What you get when you tell Python to create a class.
# def How you define  a function inside a class.
# self Inside the functions in a class, self is a variable for the instance/object being accessed.
# inheritance The concept that one class can inherit traits from another class, much like you and your parents.
# composition The concept that a class can be composed of other classes as parts, much like how a car has wheels.
# attribute A property classes have that are from composition and are usually variables.
# is-a A phrase to say that something inherits from another, as in a “salmon” is-a “ﬁsh.”
# has-a A phrase to say that something is composed of other things or has a trait, as in “a salmon has-a mouth.”

# classX(Y) “Make a class named X that is-a Y.”
# classX(object):def__init__(self,J) “class X has-a __init__ that takes self and J parameters.”
# classX(object):defM(self,J) “class X has-a function named M that takes self and J parameters.”
# foo=X() “Set foo to an instance of class X.”
# foo.M(J) “From foo, get the M function, and call it with parameters self, J.”
# foo.K=Q “From foo, get the K attribute, and set it to Q.”

# --------------------

import random
from urllib.request import urlopen
import sys

WORD_URL = "http://learncodethehardway.org/words.txt"
WORDS = []

PHRASES = {
    "class %%%(%%%)": "Make a class named %%% that is-a %%%",
    "class %%%(object):\n\tdef __init__(self, ***)":
    "class %%% has-a __init__ that takes self and *** params.",
    "class %%%(object):\n\tdef ***(self, @@@)":
    "class %%% has-a function *** that takes self and @@@ params.",
    "*** = %%%()":
    "Set *** to an instance of class %%%.",
    "***.***(@@@)":
    "From *** get the *** function, call it with params self, @@@.",
    "***.*** = '***'":
    "From *** get the *** attribute and set it to '***'."
    }

# do they want to dill phrases first
if len(sys.argv) == 2 and sys.argv[1] == "English":
    PHRASE_FIRST = True
else:
    PHRASE_FIRST = False

# load up the words from the website
for word in urlopen(WORD_URL).readlines():
    WORDS.append(str(word.strip(), encoding='utf-8'))


def convert(internal_snippet, internal_phrase):
    class_names = [w.capitalize() for w in random.sample(WORDS, internal_snippet.count("%%%"))]
    other_names = random.sample(WORDS, internal_snippet.count("***"))
    results = []
    param_names = []

    for i in range(0, internal_snippet.count("@@@")):
        param_count = random.randint(1, 3)
        param_names.append(', '.join(random.sample(WORDS, param_count)))

    for sentence in internal_snippet, internal_phrase:
        result = sentence[:]

        # fake class names
        for internal_word in class_names:
            result = result.replace("%%%", internal_word, 1)

        # fake  other names
        for internal_word in other_names:
            result = result.replace("***", internal_word, 1)

        # fake parameter lists
        for internal_word in param_names:
            result = result.replace("@@@", internal_word, 1)

        results.append(result)

    return results


# keep going until the hit CTRL-D

try:
    while True:
        snippets = list(PHRASES.keys())
        random.shuffle(snippets)

        for snippet in snippets:
            phrase = PHRASES[snippet]
            question, answer = convert(snippet, phrase)
            if PHRASE_FIRST:
                question, answer = answer, question

            print(question)

            input(">")
            print(f"ANSWER: {answer}\n\n")

except EOFError:
    print("\nBye")
