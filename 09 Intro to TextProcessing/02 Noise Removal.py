'''
Noise Removal
Text cleaning is a technique that developers use in a variety of domains. Depending on the goal of your project and where you get your data from, you may want to remove unwanted information, such as:

punctuation and accents
special characters
numeric digits
leading, ending, and vertical whitespace
HTML formatting
The type of noise that you need to remove from text usually depends on its source. For example, you could access data via the Twitter API, scraping a webpage, or voice recognition software. Fortunately, you can use the .sub() method in Python’s regular expression (re) library for most of your noise removal needs.

The .sub() method has three required arguments:

pattern – a regular expression that is searched for in the input string. There must be an r preceding the string to indicate it is a raw string, which treats backslashes as literal characters.
replacement_text – text that replaces all matches in the input string
input – the input string that will be edited by the .sub() method
The method returns a string with all instances of the pattern replaced by the replacement_text. Let’s see a few examples of using this method to remove and replace text from a string.

Examples
First, let’s consider how to remove HTML <p> tags from a string:

import re 

text = "<p>    This is a paragraph</p>" 

result = re.sub(r'<.?p>', '', text)

print(result) 
#    This is a paragraph
Notice, we replace the tags with an empty string ''. This is a common approach for removing text.

Next, let’s remove the whitespace from the beginning of the text. The whitespace consists of four spaces.

import re 

text = "    This is a paragraph" 

result = re.sub(r'\s{4}', '', text)

print(result) 
# This is a paragraph
Take a look at Codecademy’s Parsing with Regular Expressions lesson if you want to learn more regular expression syntax and tricks.

Instructions
1.
At the top of script.py, import the regular expression library.

2.
We used a package called Beautiful Soup to scrape The Onion website from October of 2019. We saved one of the headlines to a variable called onion_headline.

Remove the opening and closing h1 tags from onion_headline. Save the value to headline_no_tag.


Hint
Use the .sub() method to find <h1> and </h1> tags and replace them with ''. You can use '<.?h1>' to target both the opening and closing tags at one time.

3.
We also saved a Tweet to the variable tweet. Remove all @ characters. Save the result to tweet_no_at


Hint
Use the .sub() method to find @ characters and replace them with ''.

'''

import re

headline_one = '<h1>Nation\'s Top Pseudoscientists Harness High-Energy Quartz Crystal Capable Of Reversing Effects Of Being Gemini</h1>'

tweet = '@fat_meats, veggies are better than you think.'

headline_no_tag = re.sub(r'<.?h1>', '', headline_one)

tweet_no_at = re.sub(r'@', '', tweet)








try:
  print(headline_no_tag)
except:
  print('No variable called `headline_no_tag`')
try:
  print(tweet_no_at)
except:
  print('No variable called `tweet_no_at`')
