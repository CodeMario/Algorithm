def cantor(N) :
    answer = '-'
    for i in range(N) :
        answer = answer+' '*len(answer)+answer
    print(answer)

while True :
    try :
        N = int(input())
        cantor(N)
    except EOFError :
        break