def my_power(a, n):
    if n == 0:
        return 1
    if n < 0:
        return 1 / my_power(a, -n)
    if n % 2 == 0:
        return my_power(a, n // 2) * my_power(a, n // 2)
    else:
        return my_power(a, n - 1) * x

a = int(input())
n = int(input())
print(my_power(a, n))