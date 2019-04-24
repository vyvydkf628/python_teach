# -*- coding: utf-8 -*-
#  a= int(input("숫자를 입력하세요"))

#  if a % 2 ==1:
#      print("홀수입니다.")
#  else:
#      print("짝수입니다.")


# dust = int(input("미세먼지 수치를 입력해주세요 : "))
# if dust<=30:
#     print("좋음")
# elif dust<=80:
#     print("보통")
# elif dust<=150:
#     print("나쁨")
# else:
#     print("매우나쁨")

# odd = []
# even = []
# for i in range(1,11):
#     if i%2 == 0:
#         odd.append(i)
#     else:
#         even.append(i)
# print(odd,even)
# print(f'짝수리스트는 {odd}홀수리스트는 {even}')

#1 집합처럼 중복을 허용하지 않는 리스트




numbers = [2,4,6,7,4,3,1,2,3]
i=0
new_numbers=[]
for number in numbers:
    if number not in new_numbers:
        new_numbers.append(number)
       
print(new_numbers)
           
  

      
#2 fizzbuzz
# 조건
#1 만약 해당 숫자가 3으로 나누어지면 fizz
#2 만약 해당 숫자가 5로 나누어지면 'buzz'
#3 3과 5로 나눠지면 fizzbuzz

for i in range(1,101):
    if i%15 == 0:
        print('FizzBuzz')
    elif i%3 == 0:
        print("fizz")
    elif i%5==0:
        print("buzz")
    else:
        print(i)
        
        

