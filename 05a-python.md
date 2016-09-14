# Learn Python

Read Allen Downey's [Think Python](http://www.greenteapress.com/thinkpython/) for getting up to speed with Python 2.7 and computer science topics. It's completely available online, or you can buy a physical copy if you would like.

<a href="http://www.greenteapress.com/thinkpython/"><img src="img/think_python.png" style="width: 100px;" target="_blank"></a>

For quick and easy interactive practice with Python, many people enjoy [Codecademy's Python track](http://www.codecademy.com/en/tracks/python). There's also [Learn Python The Hard Way](http://learnpythonthehardway.org/book/) and [The Python Tutorial](https://docs.python.org/2/tutorial/).

---

###Q1. Lists &amp; Tuples

How are Python lists and tuples similar and different? Which will work as keys in dictionaries? Why?

Lists and tuples both hold a series of information, however tuples are "immutable" whereas lists are not. The position of a value in a tuple is important, whereas that is necessarily the case in a list.  
Additionally, although you cannot modify tuples you can replace them.  
Tuples will work as keys in dictionaries because they provide a __hash__ method.  

---

###Q2. Lists &amp; Sets

How are Python lists and sets similar and different? Give examples of using both. How does performance compare between lists and sets for finding an element. Why?

Lists and sets both contain a series of values, however sets do not contain any duplicate values and are not ordered. Sets are also hashable.  
It is faster to look through a set vs a list because searching through a set is more focused and thus takes less time. Whereas searching through a list means looking through every single value and thus takes more time the longer the list is.  
Examples:  

**SET**: A set would be useful to use if you are interested in determining the unique values in a dataset. For example if you have data from a survey taken on types of cars people drive in a city, you could use the set() function to get the different makes.  
**LIST**: For the same example above, if you wanted to order the model year of each car to find the range, a list would be useful.  


---

###Q3. Lambda Function

Describe Python's `lambda`. What is it, and what is it used for? Give at least one example, including an example of using a `lambda` in the `key` argument to `sorted`.

**Lambda** is a way to run an anonymous function and it does not need to be assigned to a variable. It is a great tool to use when you need to run a one-time function and don't want to necessarily clutter your code by creating a new function definition.  
Example:  
Letters: ['A','b','C','d']  
print sorted(Letters) --> ['A','C','b','d']  
print sorted(Letters,key=lambda letter: letter.lower()) --> ['A','b','C','d']  

---

###Q4. List Comprehension, Map &amp; Filter

Explain list comprehensions. Give examples and show equivalents with `map` and `filter`. How do their capabilities compare? Also demonstrate set comprehensions and dictionary comprehensions.

**List comprehensions** allow you to create a list using certain criteria. A 'for' loop can be rearranged directly into a list.     
**Map** applies a function to a whole list.  
**Filter** does what it's name implies--it filters a list based on inputted criteria.  

**Examples:**  
numbers = [1, 4, 7, 9, 11, 12, 18]  
squared = [n ** 2 for n in numbers if n%2==0] #returns a list of the squares from the list 'numbers' if the number is even. 
even = filter(lambda n: n%2==0, numbers) #returns the even numbers from the list 'numbers'.   
squared_all = map(lambda n: n ** 2, numbers) #returns the square of every number in the list 'numbers'.  
both = map(lambda n: n ** 2, filter(lambda n: n%2 == 0,numbers))  

**Set comprehension:**  
numbers_sq = {n**2 for n in range(14)}  

**Dictionary comprehension:**  
names = ['Dana','George','Allison','David','Alexander']  
dt_comp = {name: len(name) for name in names}  


---

###Complete the following problems by editing the files below:

###Q5. Datetime
Use Python to compute days between start and stop date.   
a.  

```
date_start = '01-02-2013'    
date_stop = '07-28-2015'
```

937 days

b.  
```
date_start = '12312013'  
date_stop = '05282015'  
```

513 days

c.  
```
date_start = '15-Jan-1994'      
date_stop = '14-Jul-2015'  
```

7850 days

Place code in this file: [q5_datetime.py](python/q5_datetime.py)

---

###Q6. Strings
Edit the 7 functions in [q6_strings.py](python/q6_strings.py)

---

###Q7. Lists
Edit the 5 functions in [q7_lists.py](python/q7_lists.py)

---

###Q8. Parsing
Edit the 3 functions in [q8_parsing.py](python/q8_parsing.py)





