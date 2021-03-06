# Part-of-Speech Tagging
To improve the performance of lemmatization, we need to find the part of speech for each word in our string. In script.py, to the right, we created a part-of-speech tagging function. The function accepts a word, then returns the most common part of speech for that word. Let’s break down the steps:

1. Import wordnet and Counter
from nltk.corpus import wordnet
from collections import Counter
wordnet is a database that we use for contextualizing words
Counter is a container that stores elements as dictionary keys
2. Get synonyms
Inside of our function, we use the wordnet.synsets() function to get a set of synonyms for the word:

def get_part_of_speech(word):
  probable_part_of_speech = wordnet.synsets(word)
The returned synonyms come with their part of speech.

3. Use synonyms to determine the most likely part of speech
Next, we create a Counter() object and set each value to the count of the number of synonyms that fall into each part of speech:

pos_counts["n"] = len(  [ item for item in probable_part_of_speech if item.pos()=="n"]  )
... 
This line counts the number of nouns in the synonym set.

4. Return the most common part of speech
Now that we have a count for each part of speech, we can use the .most_common() counter method to find and return the most likely part of speech:

most_likely_part_of_speech = pos_counts.most_common(1)[0][0]
Now that we can find the most probable part of speech for a given word, we can pass this into our lemmatizer when we find the root for each word. Let’s take a look at how we would do this for a tokenized string:

tokenized = ["How", "old", "is", "the", "country", "Indonesia"]

lemmatized = [lemmatizer.lemmatize(token, get_part_of_speech(token)) for token in tokenized]

print(lemmatized)
# ['How', 'old', 'be', 'the', 'country', 'Indonesia']
# Previously: ['How', 'old', 'is', 'the', 'country', 'Indonesia']
Because we passed in the part of speech, “is” was cast to its root, “be.” This means that words like “was” and “were” will be cast to “be”.

Instructions
1.
Navigate to the file script.py. At the top of the file, we imported get_part_of_speech for you. Use get_part_of_speech() to improve your lemmatizer.

Under the line with the lemmatized variable, use the get_part_of_speech() function in a list comprehension to lemmatize all the words in tokenized_string. Save the result to a new variable called lemmatized_pos.


Hint
Use a list comprehension with the following form to pass the token and part of speech into the lemmatizer:

lemmatized = [lemmatizer.lemmatize(token, get_part_of_speech(token)) for token in tokenized]

```python
import nltk
from nltk.corpus import wordnet
from collections import Counter

def get_part_of_speech(word):
  probable_part_of_speech = wordnet.synsets(word)
  
  pos_counts = Counter()

  pos_counts["n"] = len(  [ item for item in probable_part_of_speech if item.pos()=="n"]  )
  pos_counts["v"] = len(  [ item for item in probable_part_of_speech if item.pos()=="v"]  )
  pos_counts["a"] = len(  [ item for item in probable_part_of_speech if item.pos()=="a"]  )
  pos_counts["r"] = len(  [ item for item in probable_part_of_speech if item.pos()=="r"]  )
  
  most_likely_part_of_speech = pos_counts.most_common(1)[0][0]
  return most_likely_part_of_speech
