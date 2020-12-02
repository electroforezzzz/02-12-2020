def my_min(a, b, c, d):
  min4 = min(min(a,b),min(c,d))
  return min4
print("?")
a = int(input())
b = int(input())
c = int(input())
d = int(input())
print(my_min(a,b,c,d))