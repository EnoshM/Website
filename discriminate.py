import math

print("Enter the values for a, b, and c respectively:")
print() 
a = int(input())
b = int(input())
b = abs(b)
c = int(input())

num = (b**2) - (4*a*c)

print()
print()
num = str(num)
print("Discriminate is " + num)
print()
print()
num = int(num)

print("Properties")
print("----------")
print()

if num >= 0:
  print("• Real")
  print()

else:
  print("• Imaginary")
  exit()

if num == 0:
  print("• Equal")
  print()

else:
  print("• Unequal")
  print()

if (math.sqrt(num) % 1) == 0:
  print("• Rational")
  print()

else:
  print("• Irrational")
  print()
