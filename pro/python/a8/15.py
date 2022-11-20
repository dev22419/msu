_tuple = ('a', 'b', 'c')

_list = list(_tuple)
_list.insert(3, 'd')

new_tuple = tuple(_list)
print(new_tuple)  