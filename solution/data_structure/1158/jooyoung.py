N, K = map(int, input().split())

q = [i + 1 for i in range(N)]

result = []

while len(q) != 0:
    for _ in range(K):
        q.append(q.pop(0))
    result.append(q.pop())

print('<' + ', '.join(map(str, result)) + '>')
