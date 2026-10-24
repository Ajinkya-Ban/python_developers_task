#insert(indx,val)
lst = []
how_many_element = int(input("Enter how many element ="))
for i in range(how_many_element):
    ele = int(input(f"Enter the element {i + 1} = "))
    lst.append(ele)

print("Before inserting the element")
for j in lst:
    print(j)

#insert()
indx = input("Enter the index value = ")
if indx == "":
    print("Please enter the index number = ")
elif not indx.isdigit():
    print("Only digit allowed")

indx = int(indx)

val = input("Enter the vvalue = ")
if val == "":
    print("Enter the value")
val = int(val)
#call the insert()
lst.insert(indx,val)
# after inserting the element
print("="*50)
for k in lst:
    print(k)