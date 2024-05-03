def solution(myStr):
    answer = []
    myStr = myStr.replace('a',' ')
    myStr = myStr.replace('b',' ')
    myStr = myStr.replace('c',' ')
    myStr = myStr.strip()
    myStr = myStr.split()
    answer = myStr
    if myStr == [] :
        answer = ["EMPTY"]
    return answer