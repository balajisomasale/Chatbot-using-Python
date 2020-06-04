# Literals
The simplest text we can match with regular expressions are literals.
This is where our regular expression contains the exact text that we want to match. 
The regex a, for example, will match the text a, and the regex bananas will match the text bananas.

We can additionally match just part of a piece of text. 
Perhaps we are searching a document to see if the word monkey occurs,
since we love monkeys. We could use the regex monkey to match monkey in the piece of text 
The monkeys like to eat bananas..

Not only are we able to match alphabetical characters — digits work as well! 
The regex 3 will match the 3 in the piece of text 34, and the regex 5 gibbons will 
completely match the text 5 gibbons!

Regular expressions operate by moving character by character, from left to right,
through a piece of text. When the regular expression finds a character that matches the first piece of the expression,
it looks to find a continuous sequence of matching characters.

##Instructions
1.Each exercise in this lesson will have an interactive applet in the browser that allows you to enter a 
regular expression and see if it matches a string of text. If a character is matched, you’ll see it highlighted in green. 
If there’s a checkmark next to the string, you’ve completely matched the whole piece of text!

Enter a regular expression that matches each of the strings listed below “Match these strings” and
does NOT match any of the strings listed below “Don’t match these strings.”

When you’ve entered a regular expression that matches the appropriate strings, a key will appear in the browser. 
Each key is part of a URL that contains a surprise you can uncover when you complete the lesson! 
Add the key to the end of the URL in the code editor and run the code to unlock the next exercise. 
Move to the next exercise when you are ready!


solution:
Task is to match the words given

Add the hidden key from the browser to the end of the URL given below:

https://s3.amazonaws.com/codecademy-content/courses/regex/on
