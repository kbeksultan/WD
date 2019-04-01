import math

a = int(input())
b = int(input())

# c = math.sqrt(a*a + b*b)
c = math.hypot(a,b)

print(c)