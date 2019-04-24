# -*- coding: utf-8 -*-
#1. why do we have to use function?
# height = 30
# width = 20
# area = height * width
# perimeter = 2 *(height + width)
# print(f'직사각형의 넓이는 {area}이고 둘레는 {perimeter}')
'''
def triangle(height , width):
    area = height * width
    perimeter = 2 * (height + width)
    print(f'직사각형의 넓이는 {area}이고 둘레는 {perimeter}')
triangle(15, 15)

#2. Function concepts
def greeting():
    print('Hi')
greeting()
'''
#3. Four types of function
#3-1. parameter/returnO
def sum(a,b):
    result = a+ b
    return result
c = sum(2,4)
print(c)
#3-2  returnO
def say():
    return 'hi'
hi=say()
print(hi)
    
#3-3  parameter O
def say(name, age):
    print(f'제 이름은 {name}이고 나이는 {age}입니다.')
say('justin',19)
#3-4  parameter return X
def say():
    print("Hi")

numbers = [5,4,1,3,2]
new_numbers = numbers.sort()

new_numbers = sorted(numbers)

def maxx(a,b):
    if a>b:
        return a
    else:
        return b
        

def minn(a,b):
    if a<b:
        return a
    else:
        return b

result = maxx(5,8)
print(result)
