set={"one","two","three","four","five"}
set.remove("one")
print(set)
set.add("12")
print(set)
copied=set.copy()
print(copied)
set.clear()
print(set)

set={"one","two","three","four","five"}
set.discard("one")
print(set)
set.pop()
print(set)
print(set.union())
set.update("t")
print(set)           