from collections import deque

N, K = map(int, input().split())


def main():
    q = [i + 1 for i in range(N)]
    result = []
    num = 0
    for i in range(N):
        num += K - 1  # 2

        if num >= len(q):
            num %= len(q)

        result.append(str(q[num]))
        q.pop(num)

    print('<' + ', '.join(map(str, result)) + '>')


def main2():
    result = []
    q = deque([i + 1 for i in range(N)])
    while q:

        for _ in range(K - 1):
            q.append(q.popleft())

        result.append(q.popleft())

    print('<' + ', '.join(map(str, result)) + '>')


main()
