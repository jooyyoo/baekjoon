N = int(input())

stack = [i + 1 for i in range(N)]
while True:
    a = stack.pop(0)
    if not stack:
        print(a)
        break

    stack.append(stack.pop(0))
