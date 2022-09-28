#1

kg = input('Enter you weight in kg ')


def weight(kg):
    return int(2.2 * int(kg))


print(weight(kg))

======================================
#2

import random


def nums(count):
    for i in range(int(count)):
        print(random.randint(3, 6))


nums(50)
=======================================
#3

x = int(input('Enter first integer'))
y = int(input('Enter second integer'))


def compute(x, y):
    return abs(x - y) / (x + y)


print(compute(x, y))
========================================
#4 

year = int(input())


def leep_year(year):
  count = 0
  for i in range(1600, year, 4):
    if i % 400 == 0 or i % 100 != 0:
      count += 1
  return count

print(leep_year(year))
=========================================
#5

def perfect_number(num):
  var = 1
  sum = 0
  while var <= (num // 2):
    if num % var == 0:
      sum += var
    var += 1
  if sum == num:
    return True
  return False


for i in range(2,10000,2):
  if perfect_number(i):
    print(i)
