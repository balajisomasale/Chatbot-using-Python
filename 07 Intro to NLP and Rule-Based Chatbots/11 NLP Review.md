# NLP Review
Check out how much you’ve learned about natural language processing!

<li>Natural language processing combines computer science, linguistics, and artificial intelligence to enable computers to process human languages.
</li><li>NLTK is a Python library used for NLP.
</li><li>Text preprocessing is a stage of NLP focused on cleaning and preparing text for other NLP tasks.
</li><li>Parsing is a stage of NLP concerned with breaking up text based on syntax.
</li><li>Language models are probabilistic machine models of language use for NLP comprehension tasks. Common models include bag-of-words, n-gram models, and neural language modeling.
</li><li>Topic modeling is the NLP process by which hidden topics are identified given a body of text.
</li><li>Text similarity is a facet of NLP concerned with semblance between instances of language.
</li><li>Language prediction is an application of NLP concerned with predicting language given preceding language.
</li><li>There are many social and ethical considerations to take into account when designing NLP tools.


```python
import nltk
# Levenshtein distance:
from nltk.metrics import edit_distance

# an arbitrary plagiarism classifier:
def is_plagiarized(text1, text2):
  n = 7
  if edit_distance(text1.lower(), text2.lower()) > ((len(text1) + len(text2)) / n):
    return False
  return True

doc1 = "is this plagiarized"
doc2 = "maybe it's plagiarized"

print(is_plagiarized(doc1, doc2))
