# Alternation
Do you love baboons and gorillas? You can find either of them with the same regular expression using alternation! 
Alternation, performed in regular expressions with the pipe symbol, |, allows us 
to match either the characters preceding the | OR the characters after the |. 
The regex baboons|gorillas will match baboons in the text I love baboons,
but will also match gorillas in the text I love gorillas.

Are you thinking about how to match the whole piece of text I love baboons or I love gorillas? We will get to that later on!

## Instructions
1.The interactive applet in the browser allows you to enter a regular expression and
see if it matches a string of text. If a character is matched, you’ll see it highlighted in green. 
If there’s a checkmark next to the string, you’ve completely matched the whole piece of text!

Enter a regular expression that matches each of the strings listed below “Match these strings”
and does NOT match any of the strings listed below “Don’t match these strings.”

When you’ve entered a regular expression that matches the appropriate strings, 
a key will appear in the browser. Add the key to the end of the URL in the code 
editor and run the code to unlock the next exercise!

# Solution

Task is to match two words .. so to match 2 words just add '|' between them with no space => cat|dog
