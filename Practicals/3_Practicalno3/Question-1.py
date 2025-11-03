my_list = [1, 2, 3, 4, 5]
print("Original LIST:" , my_list, '\n')

my_list.insert(2, 99)
print("After insert:", my_list, "\n")

my_list.append(6)
print("After append:", my_list, "\n")

my_list.extend([7, 8])
print("After extend:", my_list, "\n")

my_list.remove(99)
print("After remove:", my_list, "\n")

popped = my_list.pop(3)
print("After pop:", my_list, "| Popped element:", popped, "\n")

del my_list[0]
print("After del:", my_list, "\n")

temp_list = my_list.copy()
temp_list.clear()
print("After clear (copy):", temp_list, "\n")

my_list.sort()
print("After sort:", my_list, "\n")

my_list.sort(reverse=True)
print("After sort(reverse):", my_list, "\n")

my_list.reverse()
print("After reverse:", my_list, "\n")

copy_list = my_list.copy()
print("Copy of list:", copy_list, "\n")

count_5 = my_list.count(5)
print("Count of 5:", count_5, "\n")

index_5 = my_list.index(5)
print("Index of 5:", index_5, "\n")

print("Min:", min(my_list), "\n")

print("Max:", max(my_list), "\n")

print("Sum:", sum(my_list), "\n")

slice_list = my_list[1:4]
print("Sliced list [1:4]:", slice_list, "\n")
