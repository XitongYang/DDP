my_list=[1,2,3]
print(my_list[0])

my_tuple=(1,2.5,1/3)
print(my_tuple[2])

my_dict={'name':'Alice','age':25}
print(my_dict['age'])

my_set={1,2,3}
my_set.add(4)
print(my_set)

set1 = {1, 2, 3, 4, 5}
set2 = {4, 5, 6, 7, 8}

# Union
union_set = set1 | set2
print("Union:", union_set)

# Intersection
intersection_set = set1 & set2
print("Intersection:", intersection_set)

# Difference
difference_set = set1 - set2
print("Difference (set1 - set2):", difference_set)
difference_set2 = set2 - set1
print("Difference (set2 - set1):", difference_set2)