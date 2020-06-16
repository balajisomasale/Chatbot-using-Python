# Review
This lesson is not an exhaustive introduction to text preprocessing. However, it does show a few of the most common tricks for cleaning your data. Before building a text preprocessing pipeline, it’s most important to have an idea of how you want your data formatted and why you want it formatted that way. Once you know what you want, you can use these tools to get you there.

Let’s review what we covered in this lesson:

Text preprocessing is all about cleaning and prepping text data so that it’s ready for other NLP tasks.
Noise removal is a text preprocessing step concerned with removing unnecessary formatting from our text.
Tokenization is a text preprocessing step devoted to breaking up text into smaller units (usually words or discrete terms).
Normalization is the name we give most other text preprocessing tasks, including stemming, lemmatization, upper and lowercasing, and stopword removal.
Stemming is the normalization preprocessing task focused on removing word affixes.
Lemmatization is the normalization preprocessing task that more carefully brings words down to their root forms.
Instructions
To the right, we added some HTML text that we pulled from Oprah Winfrey’s Wikipedia page. See if you can use only the skills you’ve learned in this lesson to:

Select only the string within the <h1> tags.
Remove all periods
Make all of the words lowercase.
Tokenize the string
Lemmatize the string


```python
from nltk.tokenize import word_tokenize, sent_tokenize
from nltk.stem import WordNetLemmatizer
from part_of_speech import get_part_of_speech
import re

lemmatizer = WordNetLemmatizer()

oprah_wiki = '<p>Working in local media, she was both the youngest news anchor and the first black female news anchor at Nashville\'s WLAC-TV. </p>'

oprah_edited_text = re.sub(r'</?p>', '', oprah_wiki)
text_no_periods = re.sub(r'\.', '', oprah_edited_text).lower()

tokenized_string = word_tokenize(text_no_periods)

lemmatized_pos = [lemmatizer.lemmatize(token, get_part_of_speech(token)) for token in tokenized_string]
