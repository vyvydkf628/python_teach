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
# def sum(a,b):
#     result = a+ b
#     return result
# c = sum(2,4)
# print(c)
# #3-2  returnO
# def say():
#     return 'hi'
# hi=say()
# print(hi)
    
# #3-3  parameter O
# def say(name, age):
#     print(f'제 이름은 {name}이고 나이는 {age}입니다.')
# say('justin',19)
# #3-4  parameter return X
# def say():
#     print("Hi")

# numbers = [5,4,1,3,2]
# new_numbers = numbers.sort()

# new_numbers = sorted(numbers)

# def maxx(a,b):
#     if a>b:
#         return a
#     else:
#         return b
        

# def minn(a,b):
#     if a<b:
#         return a
#     else:
#         return b

# result = maxx(5,8)
# print(result)





# def greeting(age, name='jeju'):
    
#     print(f'{name}은 {age}살 입니다.')
    
# greeting(19)
# greeting(19,"justin")
# greeting(age=19,name="bab")
# greeting(name="bab",age=19)
# greeting(name='철수',19)

# print("hi","hi",sep='-')

# def my_func(*args):
#     print(args)
#     print(type(args))
#     return args
    
# my_func(1,2,3)
# my_func(1,2,3,4,5)
# my_func(1,'a',[1,2,3],(1,2,3),{'a':1,'b':2})

# def my_dcit(**kwargs):
#     print(kwargs)
#     print(typq(kwargs))

# my_dcit(korean="안녕하세요",english='hi',중국어='nihao')
# my_dcit(korean="안녕하세요",english='hi',중국어='nihao',스페인어 = 'adios')

# example 1
# 사용자의 입력 값을 받아서 , 그 수가 짝홀수 구분 함수
def oddeven():
    a= int(input("값을 입력하세요 ."))
    if a%2==0:
        print(a,"는 짝수 입니다.")
    else:
        print(a,"는 홀수입니다.")
oddeven()

# 리스트 안의 가장 작은 요소를 출력
items = [1,2,-8,0]
def minmin():
    min_num= items[0]
    for item in items:
        if item <min_num:
            min_num= item
    print(a)
minmin()


# 양의 정수의 합

def pos_sum(*args):
    sum=0
    for pos in args:
        if pos >0:
            sum+=pos
    print(sum)
pos_sum(1,5,10,-4)











