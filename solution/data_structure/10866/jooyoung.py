import sys
from collections import deque


def input():
    return sys.stdin.readline().rstrip()


N = int(input())
dq = deque()
result = ""
for testcase in range(N):
    todo = input().split()
    num = 0
    if len(todo) == 2:
        num = todo[1]
    todo = todo[0]

    if todo == "push_front":
        dq.appendleft(num)
    elif todo == "push_back":
        dq.append(num)
    elif todo == "pop_front":
        if len(dq) > 0:
            result += str(dq.popleft()) + "\n"
        else:
            result += "-1\n"

    elif todo == "pop_back":
        if len(dq) > 0:
            result += str(dq.pop()) + "\n"
        else:
            result += "-1\n"
    elif todo == "size":
        result += str(len(dq)) + "\n"

    elif todo == "empty":
        if len(dq) == 0:
            result += "1\n"
        else:
            result += "0\n"
    elif todo == "front":
        if len(dq) > 0:
            result += str(dq[0]) + "\n"
        else:
            result += "-1\n"
    elif todo == "back":
        if len(dq) > 0:
            result += str(dq[-1]) + "\n"
        else:
            result += "-1\n"

print(result)
