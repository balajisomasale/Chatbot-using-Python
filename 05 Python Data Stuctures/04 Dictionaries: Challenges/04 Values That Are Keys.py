'''
Create a function named values_that_are_keys that takes a dictionary named my_dictionary as a parameter. 
This function should return a list of all values in the dictionary that are also keys.
'''

  
# Write your values_that_are_keys function here:
def values_that_are_keys(my_dictionary):
    result=[]
    for key,value in my_dictionary.items():
        for item in my_dictionary.keys():
            if item==value:
                result.append(value)
    return result
# Uncomment these function calls to test your  function:
print(values_that_are_keys({1:100, 2:1, 3:4, 4:10}))
# should print [1, 4]
print(values_that_are_keys({"a":"apple", "b":"a", "c":100}))
# should print ["a"]

