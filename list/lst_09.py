lst = [55,77,78,99,12]
#pop()
# popped_ele = lst.pop()
# print(popped_ele)
# print(lst)

#pop(index)
# indx = int(input("Enter the index number = "))
# if indx > len(lst) or indx < len(lst):
#     print("Please check index number")
# else:
#     popped_ele = lst.pop(20)
#     print(lst)

#remove()

val = int(input("Enter the value to be remove = "))
if val not in lst:
    print("Please check the value")
else:
    lst.remove(val)
    print(lst)
