# Language Models - Bag-of-Words Approach
How can we help a machine make sense of a bunch of word tokens? 
We can help computers make predictions about language by training a language model on a corpus (a bunch of example text).

Language models are probabilistic computer models of language.
We build and use these models to figure out the likelihood that a given sound, letter, word, or phrase will be used. Once a model has been trained, it can be tested out on new texts.

One of the most common language models is the unigram model, a statistical language model commonly known as bag-of-words. As its name suggests, bag-of-words does not have much order to its chaos! 
What it does have is a tally count of each instance for each word. Consider the following text example:

Provided some initial preprocessing, bag-of-words would result in a mapping like:

{"the": 2, "squid": 1, "jump": 1, "out": 1, "of": 1, "suitcase": 1}
Now look at this sentence and mapping: “Why are your suitcases full of jumping squids?”

{"why": 1, "be": 1, "your": 1, "suitcase": 1, "full": 1, "of": 1, "jump": 1, "squid": 1}
You can see how even with different word order and sentence structures, “jump,” “squid,” 
and “suitcase” are shared topics between the two examples. 
Bag-of-words can be an excellent way of looking at language when you want to make predictions concerning topic or sentiment of a text. 
When grammar and word order are irrelevant, this is probably a good model to use.

```python

# importing regex and nltk
import re, nltk
from nltk.corpus import stopwords
from nltk.tokenize import word_tokenize
from nltk.stem import WordNetLemmatizer
# importing Counter to get word counts for bag of words
from collections import Counter
# importing a passage from Through the Looking Glass
from looking_glass import looking_glass_text
# importing part-of-speech function for lemmatization
from part_of_speech import get_part_of_speech

# Change text to another string: => text = "Such an excellent bag of words and an excellent word 'bags'."
text = looking_glass_text

cleaned = re.sub('\W+', ' ', text).lower()
tokenized = word_tokenize(cleaned)

stop_words = stopwords.words('english')
filtered = [word for word in tokenized if word not in stop_words]

normalizer = WordNetLemmatizer()
normalized = [normalizer.lemmatize(token, get_part_of_speech(token)) for token in filtered]
# Comment out the print statement below
#print(normalized)

# Define bag_of_looking_glass_words & print:
bag_of_looking_glass_words=Counter(normalized)
print(bag_of_looking_glass_words)
