# user input
lst = []
how_many_ele = int(input("Enter how many element you want = "))
for i in range(how_many_ele):
    ele = int(input(f"Enter the element of {i + 1} = "))
    lst.append(ele)

print(lst)
