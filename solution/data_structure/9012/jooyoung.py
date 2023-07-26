N = int(input())
result = ""
for i in range(N):
    parenthesis = input()
    cnt = 0

    for p in parenthesis:  # 괄호 수 만큼 for 문 돌기
        cnt += 1 if p == "(" else -1

        if cnt < 0:
            result += "NO\n"
            break

    else: # for 문에서 break 를 만나지 않았을 때 실행 된다
        if cnt == 0:
            result += "YES\n"
        else:
            result += "NO\n"
print(result)
