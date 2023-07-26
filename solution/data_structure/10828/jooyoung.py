N = int(input())

stack = []

for i in range(N):
    todo = input().split()
    num = 0
    if len(todo) == 2:
        num = todo[1]
    todo = todo[0]

    if todo == "push":
        stack.append(num)

    elif todo == "top":
        if len(stack) > 0:
            print(stack[-1])
        else:
            print(-1)

    elif todo == "size":
        print(len(stack))

    elif todo == "empty":
        if len(stack) > 0:
            print(0)
        else:
            print(1)

    elif todo == "pop":
        if len(stack) > 0:
            print(stack.pop())
        else:
            print(-1)
