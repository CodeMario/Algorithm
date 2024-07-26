def solution(phone_book):
    answer = True
    if len(phone_book) != 1:
        phone_book.sort(key=lambda x : x)
        for i in range(len(phone_book)-1):
            if phone_book[i] in phone_book[i+1][:len(phone_book[i])]:
                answer = False
                break
    return answer