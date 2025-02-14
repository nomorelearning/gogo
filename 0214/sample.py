list1 = [1,2,3,4]
list2 = [5,6,7,8]

array = [[] for _ in range(2)]

array[0].extend(list1)
array[1].extend(list2)
print(array)