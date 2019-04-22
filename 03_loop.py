# n= 0 
# while n<5:
#     print('저의 꿈은 한량입니다.')
# #     n+=1
# foods = ['pizza','pasta','rice']
# for food in foods:
#     print(food)
n=-1
new_numbers=[]
numbers = [1,2,3,4,5,6]
for number in numbers:
    number*=2
    print(number)
    n=n+1
    new_numbers.append(number)
print(new_numbers)
for i in range(9):
    print(i+1,"단: ",end=" ")
    for j in range(9):
        print((i+1)*(j+1),end=",")
    print("")

