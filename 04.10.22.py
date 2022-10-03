#1

str1 = ''
for i in range(5):
  a = input("Enter a number ")
  while not a.isdigit():
    a = input("Enter only number ")
  str1 += '+' + a
print(str1[1:])
====================================
#2

phone = input('Enter phone number')
lst_phone = phone.split('-')
for i in lst_phone:
  if not i.isdigit:
    print('Invalid')
if len(lst_phone) == 4:
  if len(lst_phone[0]) == 1 and len(lst_phone[1]) == 3 and len(lst_phone[2]) == 3 and len(lst_phone[3]) == 4:
    print('Valid')
  else:
    print('Invalid')
elif len(lst_phone) == 3:
  if len(lst_phone[0]) == 3 and len(lst_phone[1]) == 3 and len(lst_phone[2]) == 4:
      print('Valid')
  else:
    print('Invalid')
else:
  print('Invalid')
=====================================
#3

a = [i for i in range(100, 1000) if str(i) == str(i)[::-1] ]
print(a)
======================================
#4

L=[2,3,5,7,11,13,17,19,23,29,31,37,41,43,47]
gaps = []
count_1 = 0
for i in range(len(L) - 1):
  gaps.append(L[i + 1] - L[i] - 1)
for i in gaps:
  if i == 1:
    count_1 += 1
print(max(gaps))
print((100 * count_1) / len(L))
======================================
#5

def productes():
  dct = {}
  while True:
    key = input("your product name ")
    if key == 'exit':
      break
    value = input("price of product")
    dct[key] = value
  return dct.get(input("Enter your product "),"this product not found")

print(productes())
========================================
#6

di = [{'name':'Todd', 'phone':'555-1414', 'email':'todd@mail.net'},
{'name':'Helga', 'phone':'555-1618', 'email':'helga@mail.net'}, {'name':'Princess', 'phone':'555-3141' , 'email':''},
{'name':'LJ', 'phone':'555-2718', 'email':'lj@mail.net'}]


for i in di:
  if i['phone'][-1] == '8' or i['email'] == '':
    print(i['name'])
=========================================
#7

matrix = [[24,67,31],[47,24,67],[31,31,13]]
dct = {}
for i in matrix:
  for j in i:
   dct[j] = dct.get(j,0) + 1


for i in range(3):
  print(list(dct.keys())[list(dct.values()).index(max(list(dct.values())))])
  del dct[list(dct.keys())[list(dct.values()).index(max(list(dct.values())))]]
  
