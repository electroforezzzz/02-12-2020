a = ['Yurii Grinkov 20', 'Maria Kuznetsova 19', 'Reter Petrov 21', 'Ivan Ivanov 23']
a = sorted(a, key = lambda x: int(x[-2]))
b = a[0]
for i in range(0, len(a) - 1):
  if a[i] < b:
     b = a[i]
print(b)