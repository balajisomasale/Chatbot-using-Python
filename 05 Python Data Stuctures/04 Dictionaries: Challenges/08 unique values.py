'''
  Create a function named unique_values that takes a dictionary named my_dictionary as a parameter. 
  The function should return the number of unique values in the dictionary.


Hint
Begin by creating a new empty list named seen_values. Loop through all of the values of my_dictionary. 
For every value, check to see if that value is in seen_values. If it is, continue to the next value. 
If it is not, add it to seen_values. After looping through all values, return the length of seen_values.
'''

# Write your unique_values function here:

def unique_values(my_dictionary):
    seenvalues=[]
    for value in my_dictionary.values():
        if value not in seenvalues:
            seenvalues.append(value)
    return len(seenvalues)
# Uncomment these function calls to test your  function:
print(unique_values({0:3, 1:1, 4:1, 5:3}))
# should print 2
print(unique_values({0:3, 1:3, 4:3, 5:3}))
# should print 1
