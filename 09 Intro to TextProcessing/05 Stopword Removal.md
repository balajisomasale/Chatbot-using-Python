# Stopword Removal
Stopwords are words that we remove during preprocessing when we don’t care about sentence structure. They are usually the most common words in a language and don’t provide any information about the tone of a statement. They include words such as “a”, “an”, and “the”.

NLTK provides a built-in library with these words. You can import them using the following statement:

```python
from nltk.corpus import stopwords 
stop_words = set(stopwords.words('english')) 
We create a set with the stop words so we can check if the words are in a list below.

Now that we have the words saved to stop_words, we can use tokenization and a list comprehension to remove them from a sentence:

nbc_statement = "NBC was founded in 1926 making it the oldest major broadcast network in the USA"

word_tokens = word_tokenize(nbc_statement) 
# tokenize nbc_statement

statement_no_stop = [word for word in word_tokens if word not in stop_words]

print(statement_no_stop)
# ['NBC', 'founded', '1926', 'making', 'oldest', 'major', 'broadcast', 'network', 'USA']

```
In this code, we first tokenized our string, nbc_statement, then used a list comprehension to return a list with all of the stopwords removed.

Instructions
1.
At the top of your script, import stopwords from NLTK. Save all English stopwords, as a set, to a variable called stop_words.


Hint
Use the following code to import stopwords:
```python
from nltk.corpus import stopwords 
Then, create a set of English stopwords with the following:

stop_words = set(stopwords.words('english')) 
```
2.
Tokenize the text in survey_text and save the result to tokenized_survey.


Hint
Use word_tokenize() to tokenize survey_text, by word.

3.
Remove stop words from tokenized_survey and save the result to text_no_stops.


Hint
Use a list comprehension of the following form:

my_var = [w for w in word_tokens if not w in stop_words]
Substitute tokenized_survey for word_tokens.

# Solution
```python
from nltk.tokenize import word_tokenize

from nltk.corpus import stopwords

survey_text = 'A YouGov study found that American\'s like Italian food more than any other country\'s cuisine.'



stop_words=set(stopwords.words('english'))




tokenized_survey=word_tokenize(survey_text)

text_no_stops=[w for w in tokenized_survey if not w in stop_words]


try:
  print(f'Stopwords type: {type(stop_words)}')
except:
  print('Expected a variable called `stop_words`')
try:
  print(f'Words Tokenized: {tokenized_survey}')
except:
  print('Expected a variable called `tokenized_survey`')
try:
  print(f'Text without Stops: {text_no_stops}')
except:
  print('Expected a variable called `text_no_stops`')
  
