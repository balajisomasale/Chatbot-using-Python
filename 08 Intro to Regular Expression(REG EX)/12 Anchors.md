#Anchors
When writing regular expressions, it’s useful to make the expression as specific as possible in order to ensure that we do not match unintended text. To aid in this mission of specificity, we can use the anchor metacharacters. The anchors hat ^ and dollar sign $ are used to match text at the start and the end of a string, respectively.

The regex ^Monkeys: my mortal enemy$ will completely match the text Monkeys: my mortal enemy but not match Spider Monkeys: my mortal enemy in the wild or Squirrel Monkeys: my mortal enemy in the wild. The ^ ensures that the matched text begins with Monkeys, and the $ ensures the matched text ends with enemy.

Without the anchor tags, the regex Monkeys: my mortal enemy will match the text Monkeys: my mortal enemy in both Spider Monkeys: my mortal enemy in the wild and Squirrel Monkeys: my mortal enemy in the wild.

Once again, as with all other metacharacters, in order to match the symbols ^ and $, you need to use the escape character in your regex. The regex My spider monkey has \$10\^6 in the bank will completely match the text My spider monkey has $10^6 in the bank.

Instructions
1.The interactive applet in the browser allows you to enter a regular expression and see if it matches a string of text. If a character is matched, you’ll see it highlighted in green. If there’s a checkmark next to the string, you’ve completely matched the whole piece of text!

Enter a regular expression that matches each of the strings listed below “Match these strings” and does NOT match any of the strings listed below “Don’t match these strings.”

When you’ve entered a regular expression that matches the appropriate strings, a key will appear in the browser. Add the key to the end of the URL in the code editor and run the code to unlock the next exercise!

With this last key, you have the complete URL! Before proceeding to the next exercise,
open the link in a new tab and see your surprise :)

# Solutions 

    Regex : ^penguins are cooler than regular expressions    
    among
    Match this string
🚫penguins are cooler than regular expressions
Don't match these strings
🚫king penguins are cooler than regular expressions
🚫penguins are cooler than regular expressions!
