def my_div(h):
  if h == 1:
    return h
  else:
    for i in range(1,h):
      if (h % i == 0):
        max = i
      if (max == 1):
        max = h
    return max

print("?")

h = int(input())

print(my_div(h))