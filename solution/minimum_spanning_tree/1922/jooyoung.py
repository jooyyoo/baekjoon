'''
1922 크루스칼 알고리즘

'''

N = int(input())
M = int(input())
parent = [i for i in range(1, 7)]
connect_stack = []
for i in range(M):
    a, b, c = map(int, input().split())  # 연결 된 간선(a-b)과 그 가중치(c)
    connect_stack.append((a, b, c))

connect_stack.sort(key=lambda x: x[-1])

# 사이클을 형성하지 않는 선에서 정렬된 순서대로 간선을 선택한다
for i in range(M):
    #부모 노드 확인
    if parent[connect_stack[0][0]] != parent[connect_stack[0][1]]:
        pass
