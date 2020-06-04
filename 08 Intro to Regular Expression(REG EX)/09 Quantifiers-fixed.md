# Quantifiers - Fixed
Here’s where things start to get really interesting. So far we have only matched text on a character by character basis. 
But instead of writing the regex \w\w\w\w\w\w\s\w\w\w\w\w\w, 
which would match 6 word characters, followed by a whitespace character, 
and then followed by more 6 word characters, such as in the text rhesus monkey,
is there a better way to denote the quantity of characters we want to match?

The answer is yes, with the help of quantifiers! Fixed quantifiers,
denoted with curly braces {}, let us indicate the exact quantity of a character we wish to match,
or allow us to provide a quantity range to match on.

\w{3} will match exactly 3 word characters
\w{4,7} will match at minimum 4 word characters and at maximum 7 word characters
The regex roa{3}r will match the characters ro followed by 3 as, and then the character r,
such as in the text roaaar. The regex roa{3,7}r will match the characters ro followed by 
at least 3 as and at most 7 as, followed by an r, matching the strings roaaar, roaaaaar and roaaaaaaar.

An important note is that quantifiers are considered to be greedy. This means that they will match the greatest quantity of characters they possibly can. For example, the regex mo{2,4} will match the text moooo in the string moooo, and not return a match of moo, or mooo. This is because the fixed quantifier wants to match the largest number of os as possible, which is 4 in the string moooo.

## Instructions
1.The interactive applet in the browser allows you to enter a regular expression and see if it matches a string of text. If a character is matched, you’ll see it highlighted in green. If there’s a checkmark next to the string, you’ve completely matched the whole piece of text!

Enter a regular expression that matches each of the strings listed below “Match these strings” and does NOT match any of the strings listed below “Don’t match these strings.”

When you’ve entered a regular expression that matches the appropriate strings, a key will appear in the browser. 
Add the key to the end of the URL in the code editor and run the code to unlock the next exercise!

#Solution :
  Regex : squea{3,5}k
