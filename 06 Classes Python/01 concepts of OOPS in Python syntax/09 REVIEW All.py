'''Review
In this lesson, we learned more complicated relationships between classes. We learned:

How to create a subclass of an existing class.
How to redefine existing methods of a parent class in a subclass by overriding them.
How to leverage a parent class’s methods in the body of a subclass method using the super() function.
How to define a Python exception that inherits from Exception.
How to write programs that are flexible using interfaces and polymorphism.
How to write data types that look and feel like native data types with dunder methods.
These are really complicated concepts! 
It’s a long journey to get to the state of comfortably being able to build class hierarchies that
embody the concerns that your software will need to. Give yourself a pat on the back, you earned it!

Instructions
1.
Create a class SortedList that inherits from the built-in type list.

2.
Recall that lists have a .append() method that takes a two arguments, self and value. We’re going to have SortedList perform a sort after every .append().

Overwrite the append method, leave it blank for now with the pass keyword.

3.
First, we want our new .append() to actually add the item to the list.

Write the code that would get SortedList to behave like a normal list when calling the .append() method.


Stuck? Get a hint
4.
After you’ve appended the new value, sort the list.


Stuck? Get a hint
5.
Incredible! We subclassed a Python primitive and introduced new behavior to it.

Some things to consider:

When a SortedList gets initialized with unsorted values (say if you call SortedList([4, 1, 5])) 
those values don’t get sorted! How would you change SortedList 
so that the list is sorted right after the object gets created?
'''


class SortedList(list):
  def append(self, value):
    super().append(value)
    self.sort()
What other Python builtins have functionality “missing”? Could you write a new dictionary that uses a fallback value when it tries to retrieve an item and can’t?
