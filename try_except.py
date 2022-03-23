#problems1

#TypeError
# a = int(input('Введите число: '))
# b = 's'
# print(a+b)

#IndexError
# n = [1,2,3,4]
# print(n[5])

#NameError
# s = 'Hello'
# print(c)

#problems2
try:
  at = 10
  iin = 15
  wo = 20
  
  for e in range(-at, at):
    print(wo / e)
    if at > '5':
      print('at > 5')

except TypeError:
  print('Ошибка типов')

#problems3
lst = []
try:
  for i in range(10):
    lst.append(i)
    a = list(reversed(lst))
    sls_obj = slice('0','8')
  print(a[sls_obj])
except TypeError:
  print('Ошибка в виде типов типами')

#prolems4
try:
  a = (0)
  b = (1)
  numbers = []
  while b > a:
    numbers += b
    b += 1
except TypeError:
  print('Ошибка типа данных')