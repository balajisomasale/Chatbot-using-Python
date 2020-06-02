'''
Write a function named word_length_dictionary that takes a list of strings named words as a parameter. 
The function should return a dictionary of key/value pairs where every key is a word in words and every value is the length of that word.


Hint
First create an empty dictionary named something like word_lengths. 
Loop through every word in words and add a new key using word_lengths[word] = len(word)
'''

# Write your word_length_dictionary function here:
def word_length_dictionary(words):
    result={}
    for word in words:
        result[word]=len(word)

        
    return result
# Uncomment these function calls to test your  function:
print(word_length_dictionary(["apple", "dog", "cat"]))
# should print {"apple":5, "dog": 3, "cat":3}
print(word_length_dictionary(["a", ""]))
# should print {"a": 1, "": 0}
