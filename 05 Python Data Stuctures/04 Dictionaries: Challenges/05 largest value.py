'''

Write a function named max_key that takes a dictionary named my_dictionary as a parameter. 
The function should return the key associated with the largest value in the dictionary.
''''

HInt: Begin by creating two variables named largest_key and largest_value. Initialize largest_value to be the smallest number possible (you can use float("-inf"). Initialize largest_key to be an empty string.

Loop through all keys/value pair in the dictionary. Any time you find a value larger than what is currently stored in largest_value, replace largest_value with that new value. Similarly, replace largest_key with the key associated with the new largest value.

After looping through all key/value pairs, return largest_key.

# Write your max_key function here:
def max_key(my_dictionary):
  largest_key = float("-inf")
  largest_value = float("-inf")
  for key, value in my_dictionary.items():
    if value > largest_value:
      largest_value = value
      largest_key = key
  return largest_key

# Uncomment these function calls to test your  function:
print(max_key({1:100, 2:1, 3:4, 4:10}))
# should print 1
print(max_key({"a":100, "b":10, "c":1000}))
# should print "c"
