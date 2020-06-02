'''
Write a function named frequency_dictionary that takes a list of elements named words as a parameter. 
The function should return a dictionary containing the frequency of each element in words.


Hint
First, create a new empty dictionary. Then, loop through every word in words. 
If word is not a key in the dictionary, make word a key with a value of 1. 
If word was already a key, increase the value associated with word by 1.

'''
# Write your frequency_dictionary function here:

def frequency_dictionary (words):
    result={}
    for item in words:
        result[item]=words.count(item)
    return result
# Uncomment these function calls to test your  function:
print(frequency_dictionary(["apple", "apple", "cat", 1]))
# should print {"apple":2, "cat":1, 1:1}
print(frequency_dictionary([0,0,0,0,0]))
# should print {0:5}

Another Solution :
    
    def frequency_dictionary (words):
    result={}
    for item in words:
        if item in result:
            result[item]+=1
        else:
            result[item]=1
        #result[item]=words.count(item)
    return result
