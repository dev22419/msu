my_set = {1,2,3}
print(my_set)

my_set = {1.0, "Hello", (1, 2, 3)}
print(my_set)

my_set = {1,2,3,4,3,2}
print(my_set)
my_set = {1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1} # singlton set
print(my_set)

my_set = {}  #empty dictionary, not a set
print(my_set)
print(type(my_set))
 
mySet =set() #will create an empty set
print(type(mySet))
 

myList = [1,2,3,4,5]
mySet = set(myList)
print(mySet)

my_set = set([1,2,3,2])
print(my_set)


myTpl = (1,2,3,4,5,5,5,5,5)
mySet = set(myTpl)
print(mySet)

thisset = {"apple", "banana", "cherry"}
print(thisset)
 
thisset = {"apple", "banana", "cherry"}

for x in thisset:
  print(x)
thisset = {"apple", "banana", "cherry"}
print("banana" in thisset)

thisset = {"apple", "banana", "cherry"}
thisset.add("orange")
print(thisset)
 
thisset = {"apple", "banana", "cherry"}
print(len(thisset))

thisset = {"apple", "banana", "cherry"}
thisset.remove("banana")
print(thisset)

thisset = {"apple", "banana", "cherry"}
thisset.discard("banana")
print(thisset)
thisset = {"apple", "banana", "cherry"}
x = thisset.pop()
 
print(x)
print(thisset)
thisset = {"apple", "banana", "cherry"}

thisset.clear()
print(thisset)
 
thisset = {"apple", "banana", "cherry"}
del thisset
print(thisset)

set1 = {"a", "b" , "c"}
set2 = {1, 2, 3}
set3 = set1.union(set2)
print(set3)

set1 = {"a", "b" , "c"}
set2 = {1, 2, 3}
set1.update(set2)
print(set1)
  
thisset = set(("apple", "banana", "cherry")) # note the double round-brackets
print(thisset)
