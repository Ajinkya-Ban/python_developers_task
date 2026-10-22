s1 = int(input("ENTER THE FIRST SIDE: "))
s2 = int(input("ENTER THE SECOND SIDE: "))
s3 = int(input("ENTER THE THIRD SIDE: "))

if s1 <= 0 or s2 <= 0 or s3 <= 0:
    print("SIDE LENGTHS MUST BE POSITIVE")
elif s1 + s2 <= s3 or s1 + s3 <= s2 or s2 + s3 <= s1:
    print("THIS IS NOT A VALID TRIANGLE")
elif s1 == s2 == s3:
    print("THIS IS EQUILATERAL TRIANGLE")
elif s1 == s2 or s2 == s3 or s1 == s3:
    print("THIS IS ISOSCELES TRIANGLE")
else:
    print("THIS IS SCALENE TRIANGLE")
