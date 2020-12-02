a = int(input())
b = int(input())
def my_sum(a,b):
    a += 1
    b -= 1
    if b != 0:
        return my_sum(a,b)
    else:
        return a
print(my_sum(a,b))