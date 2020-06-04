# Shorthand Character Classes
While character ranges are extremely useful, they can be cumbersome to write out every 
single time you want to match common ranges such as those that designate alphabetical characters or digits.
To alleviate this pain, there are shorthand character classes that represent common ranges, 
and they make writing regular expressions much simpler. These shorthand classes include:

\w: the “word character” class represents the regex range [A-Za-z0-9_], and it matches a single 
uppercase character, lowercase character, digit or underscore
\d: the “digit character” class represents the regex range [0-9], and it matches a single digit character
\s: the “whitespace character” class represents the regex range [ \t\r\n\f\v], matching a single space, 
tab, carriage return, line break, form feed, or vertical tab
For example, the regex \d\s\w\w\w\w\w\w\w matches a digit character, followed by a whitespace character,
followed by 7 word characters. Thus the regex completely matches the text 3 monkeys.

In addition to the shorthand character classes \w, \d, and \s, we also have access to the negated 
shorthand character classes! These shorthands will match any character that is NOT in the regular shorthand classes. 
These negated shorthand classes include:

\W: the “non-word character” class represents the regex range [^A-Za-z0-9_], matching any character that is not included in the range represented by \w
\D: the “non-digit character” class represents the regex range [^0-9], matching any character that is not included in the range represented by \d
\S: the “non-whitespace character” class represents the regex range [^ \t\r\n\f\v], matching any character that is not included in the range represented by \s
## Instructions
1.The interactive applet in the browser allows you to enter a regular expression and see if it matches a string of text. If a character is matched, you’ll see it highlighted in green. If there’s a checkmark next to the string, you’ve completely matched the whole piece of text!

Enter a regular expression that matches each of the strings listed below “Match these strings” and 
does NOT match any of the strings listed below “Don’t match these strings.”

# Soultion:
  Regex : \d\s\w\w\w\w\w\w

When you’ve entered a regular expression that matches the appropriate strings, a key will appear in the browser. Add the key to the end of the URL in the code editor and run the code to unlock the next exercise!
