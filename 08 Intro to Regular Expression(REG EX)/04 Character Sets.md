# Character Sets
Spelling tests may seem like a distant memory from grade school, but we ultimately take them every day while typing. 
It’s easy to make mistakes on commonly misspelled words like consensus,
and on top of that, there are sometimes alternate spellings for the same word.

Character sets, denoted by a pair of brackets [], 
let us match one character from a series of characters, 
allowing for matches with incorrect or different spellings.

The regex con[sc]en[sc]us will match consensus, 
the correct spelling of the word, but also match the following three incorrect 
spellings: concensus, consencus, and concencus. The letters inside the first brackets,
s and c, are the different possibilities for the character that comes after con and before en. 
Similarly for the second brackets, s and c are the different character possibilities to come after en and before us.

Thus the regex [cat] will match the characters c, a, or t, but not the text cat.

The beauty of character sets (and alternation) is that they allow our regular expressions to
become more flexible and less rigid than by just matching with literals!

We can make our character sets even more powerful with the help of the caret ^ symbol.
Placed at the front of a character set, the ^ negates the set, matching any character
that is not stated. These are called negated character sets. Thus the regex [^cat] will match any 
character that is not c, a, or t, and would completely match each character d, o or g.

Do we have a consensus that regular expressions are pretty cool?

## Instructions
1.The interactive applet in the browser allows you to enter a regular expression and 
see if it matches a string of text. If a character is matched, you’ll see it highlighted in green. 
If there’s a checkmark next to the string, you’ve completely matched the whole piece of text!

Enter a regular expression that matches each of the strings listed below “Match these strings”
and does NOT match any of the strings listed below “Don’t match these strings.”

When you’ve entered a regular expression that matches the appropriate strings, a key will appear in the browser.
Add the key to the end of the URL in the code editor and run the code to unlock the next exercise!

# Solution : 
cat|dog|rat => just keep or symbol between the words to be matched
