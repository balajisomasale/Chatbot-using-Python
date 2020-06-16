# Tokenization
For many natural language processing tasks, we need access to each word in a string. To access each word, we first have to break the text into smaller components. The method for breaking text into smaller components is called tokenization and the individual components are called tokens.

A few common operations that require tokenization include:

Finding how many words or sentences appear in text
Determining how many times a specific word or phrase exists
Accounting for which terms are likely to co-occur
While tokens are usually individual words or terms, they can also be sentences or other size pieces of text.

To tokenize individual words, we can use nltk‘s word_tokenize() function. The function accepts a string and returns a list of words:
```python
from nltk.tokenize import word_tokenize

text = "Tokenize this text"
tokenized = word_tokenize(text)

print(tokenized)
# ["Tokenize", "this", "text"]

```
To tokenize at the sentence level, we can use sent_tokenize() from the same module.


```python
from nltk.tokenize import sent_tokenize

text = "Tokenize this sentence. Also, tokenize this sentence."
tokenized = sent_tokenize(text)

print(tokenized)
# ['Tokenize this sentence.', 'Also, tokenize this sentence.']
```
Instructions
1.
Import the word_tokenize() and sent_tokenize() functions from Python’s NLTK package.

2.
Tokenize ecg_text by word and save the result to tokenized_by_word.


Hint
Use word_tokenize to tokenize ecg_text and save the result to tokenized_by_word.

3.
Tokenize ecg_text by sentence and save the result to tokenized_by_sentence.


Hint
Use sent_tokenize to tokenize ecg_text and save the result to tokenized_by_sentence.


# Solution :

```python
from nltk.tokenize import word_tokenize, sent_tokenize

ecg_text = 'An electrocardiogram is used to record the electrical conduction through a person\'s heart. The readings can be used to diagnose cardiac arrhythmias.'

tokenized_by_word = word_tokenize(ecg_text)

tokenized_by_sentence = sent_tokenize(ecg_text)






try:
  print('Word Tokenization:')
  print(tokenized_by_word)
except:
  print('Expected a variable called `tokenized_by_word`')
try:
  print('Sentence Tokenization:')
  print(tokenized_by_sentence)
except:
  print('Expected a variable called `tokenized_by_sentence`')
