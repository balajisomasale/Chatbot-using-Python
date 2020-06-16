# Lemmatization
Lemmatization is a method for casting words to their root forms. This is a more involved process than stemming, because it requires the method to know the part-of-speech for each word. Since lemmatization requires the part of speech, it is a less efficient approach than stemming.

In the next exercise, we will consider how to tag each word with a part of speech. In the meantime, let’s see how to use NLTK’s lemmatize operation.

We can use NLTK’s WordNetLemmatizer to lemmatize text:

```python
from nltk.stem import WordNetLemmatizer
lemmatizer = WordNetLemmatizer()
Once we have the lemmatizer initialized, we can use a list comprehension to apply the lemmatize operation to each word in a list:

tokenized = ["NBC", "was", "founded", "in", "1926"]

lemmatized = [lemmatizer.lemmatize(token) for token in tokenized]

print(lemmatized)
# ["NBC", "wa", "founded", "in", "1926"]
```
The result, saved to lemmatized contains 'wa', while the rest of the words remain the same. Not too useful. 
This happened because lemmatize() treats every word as a noun. To take advantage of the power of lemmatization, 
we need to tag each word in our text with the most likely part of speech. We’ll do that in the next exercise.

Instructions
1.
At the top of script.py, import WordNetLemmatizer, then initialize an instance of it and save the result to lemmatizer.


Hint
Use the following code to import WordNetLemmatizer.

from nltk.stem import WordNetLemmatizer
Then, create an instance of it using the following:

lemmatizer = WordNetLemmatizer()
2.
Tokenize the string saved to populated_island. Save the result to tokenized_string.


Hint
Substitute populated_island into the following code to tokenize it:

word_tokenize(words_to_tokenize)
3.
Use a list comprehension to lemmatize every word in tokenized_string. Save the result to the variable lemmatized_words.


Hint
Use a list comprehension in the following form to lemmatize every word in the tokenized list. Substitute tokenized_sentence for tokenized_string:

lemmatized = [lemmatizer.lemmatize(token) for token in tokenized_sentence]


```python
from nltk.tokenize import word_tokenize
from nltk.stem import WordNetLemmatizer
lemmatizer = WordNetLemmatizer()

populated_island = 'Indonesia was founded in 1945. It contains the most populated island in the world, Java, with over 140 million people.'

tokenized_string = word_tokenize(populated_island)

lemmatized_words = [lemmatizer.lemmatize(token) for token in tokenized_string]







try:
  print(f'A lemmatizer exists: {lemmatizer}')
except:
  print('Expected a variable called `lemmatizer`')
try:
  print(f'Words Tokenized: {tokenized_string}')
except:
  print('Expected a variable called `tokenized_string`')
try:
  print(f'Lemmatized Words: {lemmatized_words}')
except:
  print('Expected a variable called `lemmatized_words`')
  
