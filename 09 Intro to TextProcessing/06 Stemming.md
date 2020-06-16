# Stemming
In natural language processing, stemming is the text preprocessing normalization task concerned with bluntly removing word affixes (prefixes and suffixes). For example, stemming would cast the word “going” to “go”. This is a common method used by search engines to improve matching between user input and website hits.

NLTK has a built-in stemmer called PorterStemmer. You can use it with a list comprehension to stem each word in a tokenized list of words.

First, you must import and initialize the stemmer:
```python 
from nltk.stem import PorterStemmer
stemmer = PorterStemmer()
Now that we have our stemmer, we can apply it to each word in a list using a list comprehension:

tokenized = ['NBC', 'was', 'founded', 'in', '1926', '.', 'This', 'makes', 'NBC', 'the', 'oldest', 'major', 'broadcast', 'network', '.']

stemmed = [stemmer.stem(token) for token in tokenized]

print(stemmed)
# ['nbc', 'wa', 'found', 'in', '1926', '.', 'thi', 'make', 'nbc', 'the', 'oldest', 'major', 'broadcast', 'network', '.']

```
Notice, the words like ‘was’ and ‘founded’ became ‘wa’ and ‘found’, respectively. The fact that these words have been reduced is useful for many language processing applications. However, you need to be careful when stemming strings, because words can often be converted to something unrecognizable.

Instructions
1.At the top of script.py, import PorterStemmer, then initialize an instance of it and save the object to a variable called stemmer.


Hint
Use the following code to import PorterStemmer:

from nltk.stem import PorterStemmer
Then, use the following to create a variable called stemmer that is a PorterStemmer object:

stemmer = PorterStemmer()
2.
Tokenize populated_island and save the result to island_tokenized.


Hint
Pass populated_island into word_tokenize() to tokenize the text.

3.
Use a list comprehension to stem each word in island_tokenized. Save the result to a variable called stemmed.


Hint
Use code similar to the following list comprehension to stem each word in island_tokenized.

stemmed = [stemmer.stem(token) for token in tokenized]
Replace tokenized in the code above with island_tokenized.

# Solution
```python
from nltk.tokenize import word_tokenize, sent_tokenize
from nltk.stem import PorterStemmer
stemmer = PorterStemmer()

populated_island = 'Java is an Indonesian island in the Pacific Ocean. It is the most populated island in the world, with over 140 million people.'

island_tokenized = word_tokenize(populated_island)

stemmed = [stemmer.stem(token) for token in island_tokenized]








try:
  print('A stemmer exists:')
  print(stemmer)
except:
  print('Expected a variable called `stemmer`')
try:
  print('Words Tokenized:')
  print(island_tokenized)
except:
  print('Expected a variable called `island_tokenized`')
try:
  print('Stemmed Words:')
  print(stemmed)
except:
  print('Expected a variable called `stemmed`')
  
