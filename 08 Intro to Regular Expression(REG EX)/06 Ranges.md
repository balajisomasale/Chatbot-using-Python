## Ranges
Character sets are great, but their true power isn’t realized without ranges. 
Ranges allow us to specify a range of characters in which we can make a match
without having to type out each individual character. The regex [abc], 
which would match any character a, b, or c, is equivalent to regex range [a-c]. 
The - character allows us to specify that we are interested in matching a range of characters.

The regex I adopted [2-9] [b-h]ats will match the text I adopted 4 bats as
well as I adopted 8 cats and even I adopted 5 hats.

With ranges we can match any single capital letter with the regex [A-Z], 
lowercase letter with the regex [a-z], any digit with the regex [0-9].
We can even have multiple ranges in the same character set! To match any single 
capital or lowercase alphabetical character, we can use the regex [A-Za-z].

Remember, within any character set [] we only match one character.

## Instructions
1.The interactive applet in the browser allows you to enter a regular expression and 
see if it matches a string of text. If a character is matched, you’ll see it highlighted in green. 
If there’s a checkmark next to the string, you’ve gotten a match!

Enter a regular expression that matches each of the three strings listed below “Match these strings” and 
does NOT match any of the three strings listed below “Don’t match these strings.”

When you’ve entered a regular expression that matches the appropriate strings, a key will appear in the browser. 
Copy the key into the code editor and run the code to unlock the next exercise!

# Solution:
  Regex : [c-e][l-u][b-k]
