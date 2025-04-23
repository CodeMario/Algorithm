def GCD(n1, n2) :
    while (n2 != 0) :
        temp = n1 % n2
        n1 = n2
        n2 = temp

    return n1

answer = 0
N = int(input())
T = int(input())
tree = [T]
distance = []
for _ in range(N-1) :
    temp = int(input())
    tree.append(temp)
    distance.append(temp-T)
    T = temp
distance = list(set(distance))

n2 = distance[0]
for i in range(1,len(distance)) :
    n1 = distance[i]
    n2 = GCD(n1,n2)

for i in range(len(tree)-1) :
    answer += ((tree[i+1]-tree[i])//n2)-1

print(answer)