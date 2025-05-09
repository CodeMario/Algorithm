import sys
n = int(input())
A = list(map(int, sys.stdin.readline().split()))
answer = [-1] * n
stack = []

FA = {}
for i in A :
    if i in FA :
        FA[i] += 1
    else :
        FA[i] = 1

stack.append(0)
for i in range(1, n):
    while stack and FA[A[stack[-1]]] < FA[A[i]]:
        answer[stack.pop()] = A[i]
    stack.append(i)


print(*answer)