N = int(input())
result = ""
for i in range(N):
    parenthesis = input()
    cnt = 0
    for p in parenthesis:
        cnt += 1 if p == "(" else -1

        if cnt < 0:
            result += "NO\n"
            break

    if cnt == 0:
        result += "YES\n"


print(result)
