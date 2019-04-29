import requests

# res1 = requests.get("https://www.naver.com").text
# print(res1)
res2 = requests.get("https://www.naver.com").status.code
print(res2)