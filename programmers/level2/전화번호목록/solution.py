def solution(phone_book):
    answer = True

    phone_book.sort()
    for i in range(len(phone_book)-1):
        if phone_book[i+1].startswith(phone_book[i]) == True:
        # pre = len(phone_book[i])
        # nex = len(phone_book[i+1])
        # if pre < nex and phone_book[i] == phone_book[i+1][:pre]:
            answer = False
            break
                
    return answer
