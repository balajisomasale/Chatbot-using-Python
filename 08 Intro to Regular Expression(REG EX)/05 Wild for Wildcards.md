# Wild for Wildcards
Sometimes we don’t care exactly WHAT characters are in a text, just that there are SOME characters. Enter the wildcard .! 
Wildcards will match any single character (letter, number, symbol or whitespace) in a piece of text.
They are useful when we do not care about the specific value of a character, but only that a character exists!

Let’s say we want to match any 9-character piece of text. 
The regex ......... will completely match orangutan and marsupial! 
Similarly, the regex I ate . bananas will completely match both I ate 3 bananas and I ate 8 bananas!

What happens if we want to match an actual period, .? We can use the escape character, \,
to escape the wildcard functionality of the . and match an actual period. The regex Howler monkeys are really lazy\. 
will completely match the text Howler monkeys are really lazy..

## Instructions
1.The interactive applet in the browser allows you to enter a regular expression and see if it matches a string of text.
If a character is matched, you’ll see it highlighted in green. If there’s a checkmark next to the string,
you’ve completely matched the whole piece of text!

Enter a regular expression that matches each of the strings listed below “Match these strings” 
and does NOT match any of the strings listed below “Don’t match these strings.”

When you’ve entered a regular expression that matches the appropriate strings, 
a key will appear in the browser. Add the key to the end of the URL in the code editor 
and run the code to unlock the next exercise!

## Solution :
  Regex: ....\.
  Just add those dots depending on the size required tomatch the string given
