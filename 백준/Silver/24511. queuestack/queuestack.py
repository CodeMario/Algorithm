N = int(input())
qs = list(map(int, input().split()))
qsNum = list(map(int, input().split()))
M = int(input())
C = list(map(int, input().split()))[::-1]


for i in range(N) :
    if qs[i] == 0 :
        C.append(qsNum[i])

print(' '.join(map(str, C[-1:-M-1:-1])))