# Review
Do you feel those regular expression superpowers coursing through your body?
Do you just want to scream ah+ really loud? Awesome! You are now ready 
to take these skills and use them out in the wild. Before beginning your adventures,
let’s review what we’ve learned.

Regular expressions are special sequences of characters that describe a pattern of text that is to be matched
We can use literals to match the exact characters that we desire
Alternation, using the pipe symbol |, allows us to match the text preceding or following the |
Character sets, denoted by a pair of brackets [], let us match one character from a series of characters
Wildcards, represented by the period or dot ., will match any single character (letter, number, symbol or whitespace)
Ranges allow us to specify a range of characters in which we can make a match
Shorthand character classes like \w, \d and \s represent the ranges representing word characters, digit characters,
and whitespace characters, respectively
Groupings, denoted with parentheses (), group parts of a regular expression together, and allows us to
limit alternation to part of a regex
Fixed quantifiers, represented with curly braces {}, let us indicate the exact quantity or a range of quantity 
of a character we wish to match
Optional quantifiers, indicated by the question mark ?, allow us to indicate a character in a regex is optional, 
or can appear either 0 times or 1 time
The Kleene star, denoted with the asterisk *, is a quantifier that matches the preceding character 0 or more times
The Kleene plus, denoted by the plus +, matches the preceding character 1 or more times
The anchor symbols hat ^ and dollar sign $ are used to match text at the start and end of a string, respectively

# Instructions
The interactive applet in the browser allows you to enter a regular expression and see if it matches a string of text. 
If a character is matched, you’ll see it highlighted in green. If there’s a checkmark next to the string, 
you’ve completely matched the whole piece of text!

# Solution 

    Regex : 1?\s?\(?\d{3}\)?[-.\s]?\d{3}[-.\s]?\d{4}
    
    Qn : Match these strings
🚫718-555-3810
🚫9175552849
🚫1 212 555 3821
🚫(917)5551298
🚫212.555.8731
Don't match these strings
🚫wildebeest
🚫hippopotamus
🚫woolly mammoth
Enter a regular expression that matches each of the telephone numbers listed below “Match these strings”. This is a tricky one, so have some fun. Good luck!
