# reverse()
lst = [10,2,3,4,5,9,1,6,1]
# rev = []
# # lst.reverse()
# for i in range(len(lst) - 1, -1,-1):
#     rev = rev + [lst[i]]
# print(rev)

# sort()
# lst.sort() #asc
# lst.sort(reverse=True)
# print(lst)

# n = len(lst)
# for i in range(n):
#     for j in range(i + 1, n):
#         if lst[i] <  lst[j]:
#             temp = lst[i]
#             lst[i] = lst[j]
#             lst[j] = temp
# print(lst)

#index()
# val = int(input("Enter the value = "))
# if val not in lst:
#     print(f"{val} not present")
# else:
#     print(lst.index(val))

#count(val)
val = int(input("Enter the value = "))
if val not in lst:
    print(f"{val} not present")
else:
    print(lst.count(val))