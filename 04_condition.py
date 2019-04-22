# a= int(input("숫자를 입력하세요"))

# if a % 2 ==1:
#     print("홀수입니다.")
# else:
#     print("짝수입니다.")


dust = int(input("미세먼지 수치를 입력해주세요 : "))
if dust<=30:
    print("좋음")
elif dust<=80:
    print("보통")
elif dust<=150:
    print("나쁨")
else:
    print("매우나쁨")

odd = []
even = []
for i in range(1,11):
    if i%2 == 0:
        odd.append(i)
    else:
        even.append(i)
print(odd,even)