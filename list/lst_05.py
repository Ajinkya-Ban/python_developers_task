# Adding the element
lst = []
how_many_element = int(input("Enter how many element ="))
for i in range(how_many_element):
    ele = eval(input(f"Enter the element {i + 1} = "))
    lst.append(ele)

# display
for j in lst:
    print(j)
