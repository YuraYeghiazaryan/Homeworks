#1
num = input()
def is_even(num):
  if int(num) <= 0:
    return "num is not natural number"
  if int(num) % 2 == 0:
    return "num is even"
  return "num is odd"

print(is_even(num))

=============================================

#2
vowel = ['a', 'e', 'i', 'o', 'u', 'y']
char = input("enter char ")

def is_vowel(char):
  if char not in vowel:
    return char + ' is  consonant'
  return char + ' is vowel'

print(is_vowel(char))

==============================================

#3
def fib(n):
  a = 0
  b = 1
  while n > 1:
    a, b = b, b + a
    n -= 1
  return a

print(fib(6))

==============================================

#4

def sum_digits(num):
  sum = 0
  while num > 0:
    sum += num % 10
    num //= 10
  return sum

sum_digits(1087)

===============================================

#5

lst1 =[4, 2, 2, 2, 4 ]

for i in range(len(lst1)):
  if i == 0 or i == len(lst1) - 1:
    print('*' * lst1[i])
    continue
  print('*  ' * lst1[i])
