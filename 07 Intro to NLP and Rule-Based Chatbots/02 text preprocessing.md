# Text Preprocessing
"You never know what you have... until you clean your data."
~ Unknown (or possibly made up)

Cleaning and preparation are crucial for many tasks, and NLP is no exception. Text preprocessing is usually the first step you’ll take when faced with an NLP task.

Without preprocessing, your computer interprets "the", "The", and "< p>The" as entirely different words. There is a LOT you can do here, depending on the formatting you need. Lucky for you, Regex and NLTK will do most of it for you! Common tasks include:

Noise removal — stripping text of formatting (e.g., HTML tags).

Tokenization — breaking text into individual words.

Normalization — cleaning text data in any other way:

Stemming is a blunt axe to chop off word prefixes and suffixes. “booing” and “booed” become “boo”, but “sing” may become “s” and “sung” would remain “sung.”
Lemmatization is a scalpel to bring words down to their root forms. For example, NLTK’s savvy lemmatizer knows “am” and “are” are related to “be.”
Other common tasks include lowercasing, stopwords removal, spelling correction, etc.



# Instructions

1.We used NLTK’s PorterStemmer to normalize the text — run the code to see how it does. (It may take a few seconds for the code to run.)

2.In the output terminal you’ll see our program counts "go" and "went" as different words! Also, what’s up with "mani" and "hardli"? A lemmatizer will fix this. Let’s do it.

### Where lemmatizer is defined, replace None with WordNetLemmatizer().

Where we defined lemmatized, replace the empty list with a list comprehension that uses lemmatizer to lemmatize() each token in tokenized.

(Don’t know Python that well? No problem. Just check the hints for help throughout the lesson.)


Hint
### lemmatized = [lemmatizer.lemmatize(token) for token in tokenized]

3.Why are the lemmatized verbs like "went" still conjugated? By default lemmatize() treats every word as a noun.

Give lemmatize() a second argument: get_part_of_speech(token). This will tell our lemmatizer what part of speech the word is.

Run your code again to see the result!


Hint
### lemmatized = [lemmatizer.lemmatize(token, get_part_of_speech(token)) for token in tokenized]

```python
# regex for removing punctuation!
import re
# nltk preprocessing magic
import nltk
from nltk.tokenize import word_tokenize
from nltk.stem import PorterStemmer
from nltk.stem import WordNetLemmatizer
# grabbing a part of speech function:
from part_of_speech import get_part_of_speech

text = "So many squids are jumping out of suitcases these days that you can barely go anywhere without seeing one burst forth from a tightly packed valise. I went to the dentist the other day, and sure enough I saw an angry one jump out of my dentist's bag within minutes of arriving. She hardly even noticed."

cleaned = re.sub('\W+', ' ', text)
tokenized = word_tokenize(cleaned)

stemmer = PorterStemmer()
stemmed = [stemmer.stem(token) for token in tokenized]

## -- CHANGE these -- ##
lemmatizer = WordNetLemmatizer()
lemmatized = [lemmatizer.lemmatize(token,get_part_of_speech(token)) for token in tokenized]

print("Stemmed text:")
print(stemmed)
print("\nLemmatized text:")
print(lemmatized)
