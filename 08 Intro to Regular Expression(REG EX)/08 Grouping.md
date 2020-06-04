## Grouping
Remember when we were in love with baboons and gorillas a few exercises ago? 
We were able to match either baboons or gorillas using the regex baboons|gorillas, 
taking advantage of the | symbol.

But what if we want to match the whole piece of text I love baboons and I love gorillas 
with the same regex? Your first guess might be to use the regex I love baboons|gorillas.
This regex, while it would completely match the string I love baboons, would not match I love gorillas,
and would instead match gorillas. This is because the | symbol matches the entire expression before or after itself.

Grouping to the rescue! Grouping, denoted with the open parenthesis ( and the closing parenthesis ), 
lets us group parts of a regular expression together, and allows us to limit alternation to part of the regex.

The regex I love (baboons|gorillas) will match the text I love and then match either baboons or gorillas, 
as the grouping limits the reach of the | to the text within the parentheses.

These groups are also called capture groups, as they have the power to select, or capture, a substring from our matched text.

## Instructions
1.The interactive applet in the browser allows you to enter a regular expression and see if it matches a string of text. 
If a character is matched, you’ll see it highlighted in green. If there’s a checkmark next to the string, 
you’ve completely matched the whole piece of text!

Enter a regular expression that matches each of the strings listed below “Match these strings” and does NOT match any
of the strings listed below “Don’t match these strings.”

When you’ve entered a regular expression that matches the appropriate strings, a key will appear in the browser.

## Solution:
  Regex: (puppies|kitty cats) are my favorite!
Add the key to the end of the URL in the code editor and run the code to unlock the next exercise!
