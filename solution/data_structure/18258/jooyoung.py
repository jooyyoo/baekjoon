N = int(input())
queue = []
result = ""
for i in range(N):
    todo = input().split()
    num = 0

    if len(todo) == 2:
        num = todo[1]

    todo = todo[0]

    if todo == "push":
        queue.append(num)

    elif todo == "pop":
        if len(queue) > 0:
            result += str(queue.pop(0)) + "\n"
        else:
            result += "-1\n"

    elif todo == "size":
        result += str(len(queue)) + "\n"

    elif todo == "empty":
        if len(queue) == 0:
            result += "1\n"
        else:
            result += "0\n"

    elif todo == "front":
        if len(queue) == 0:
            result += "-1\n"
        else:
            result += str(queue[0]) + "\n"
    elif todo == "back":
        if len(queue) == 0:
            result += "-1\n"
        else:
            result += str(queue[-1]) + "\n"

print(result)
