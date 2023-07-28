N = int(input())  # 피연산자 개수

asc = 65

postfix = [i for i in input()]
num = dict()

for i in range(N):
    num[chr(asc)] = input()
    asc += 1

# print(postfix)
# print(num)