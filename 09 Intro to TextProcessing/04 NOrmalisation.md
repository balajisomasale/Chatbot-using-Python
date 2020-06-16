# Normalization
Tokenization and noise removal are staples of almost all text pre-processing pipelines. However, some data may require further processing through text normalization. Text normalization is a catch-all term for various text pre-processing tasks. In the next few exercises, we’ll cover a few of them:

Upper or lowercasing
Stopword removal
Stemming – bluntly removing prefixes and suffixes from a word
Lemmatization – replacing a single-word token with its root
The simplest of these approaches is to change the case of a string. We can use Python’s built-in String methods to make a string all uppercase or lowercase:
```python
my_string = 'tHiS HaS a MiX oF cAsEs'

print(my_string.upper())
# 'THIS HAS A MIX OF CASES'

print(my_string.lower())
# 'this has a mix of cases'

```
Instructions
1.
Make all the characters in brands lowercase and save the results to brands_lower.


Hint
Use the built-in .lower() string method to make all the letters in brands lowercase.

2.
Make all the letters in brands uppercase and save the results to brands_upper.


Hint
Use the built-in .upper() string method to make all the letters in brands uppercase.

```python


brands = 'Salvation Army, YMCA, Boys & Girls Club of America'

brands_lower = brands.lower()
brands_upper = brands.upper()



try:
  print(f'Lowercased brands: {brands_lower}')
except:
  print('Expected a variable called `brands_lower`')
try:
  print(f'Uppercased brands: {brands_upper}')
except:
  print('Expected a variable called `brands_upper`')
