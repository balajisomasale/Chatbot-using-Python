# Quantifiers - 0 or More, 1 or More
In 1951, mathematician Stephen Cole Kleene developed a system to match patterns in written language with mathematical notation. 
This notation is now known as regular expressions!

In his honor, the next piece of regular expressions syntax we will learn is known as the Kleene star. 
The Kleene star, denoted with the asterisk *, is also a quantifier, and matches the preceding character 0 or more times. 
This means that the character doesn’t need to appear, can appear once, or can appear many many times.

The regex meo*w will match the characters me, followed by 0 or more os, followed by a w. 
Thus the regex will match mew, meow, meooow, and meoooooooooooow.

Another useful quantifier is the Kleene plus, denoted by the plus +, which matches the preceding character 1 or more times.

The regex meo+w will match the characters me, followed by 1 or more os, followed by a w.
Thus the regex will match meow, meooow, and meoooooooooooow, but not match mew.

Like all the other metacharacters, in order to match the symbols * and +,
you need to use the escape character in your regex. The regex My cat is a \* will completely match the text My cat is a *.

# Instructions
1.The interactive applet in the browser allows you to enter a regular expression and see if it matches a string of text. 
If a character is matched, you’ll see it highlighted in green. If there’s a checkmark next to the string,
you’ve completely matched the whole piece of text!

Enter a regular expression that matches each of the strings listed below “Match these strings” and
does NOT match any of the strings listed below “Don’t match these strings.”

When you’ve entered a regular expression that matches the appropriate strings, a key will appear in the browser.
Add the key to the end of the URL in the code editor and run the code to unlock the next exercise!

# Solutions :
  Regex : hoo+t
