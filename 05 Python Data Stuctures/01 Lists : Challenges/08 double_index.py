'''
4. Double Index
Create a function named double_index that has two parameters: a list named lst and a single number named index.

The function should return a new list where all elements are the same as in lst except for the element at index. The element at index should be double the value of the element at index of the original lst.

If index is not a valid index, the function should return the original list.

For example, the following code should return [1,2,6,4] because the element at index 2 has been doubled:

double_index([1, 2, 3, 4], 2)
After writing your function, un-comment the call to the function that we’ve provided for you to test your results.

1
#W
'''

#Write your function here

def more_frequent_item(lst,item1,item2):
    i1=0
    i2=0
    first=lst.count(item1)
    second=lst.count(item2)
    
    if first>second:
        return item1
    elif second>first:
        return item2
    else:
        return item1
        
#Uncomment the line below when your function is done
print(more_frequent_item([2, 3, 3, 2, 3, 2, 3, 2, 3], 2, 3))
