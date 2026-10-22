year = int(input("ENTER A YEAR: "))

if(year%100==0):
    print("ITS A CENTURY YEAR")
    if(year % 400==0):
      print("ITS ALSO A LEAP YEAR")
    else:
      print("ITS NOT A LEAP YEAR")
elif( year%4 ==0):
      print("ITS A LEAP YEAR")
      print("ITS NOT A CENTURY YEAR")
else:
    print("IT IS NOT A LEAP YEAR")
    print("IT IS NOT A CENTURY YEAR")
