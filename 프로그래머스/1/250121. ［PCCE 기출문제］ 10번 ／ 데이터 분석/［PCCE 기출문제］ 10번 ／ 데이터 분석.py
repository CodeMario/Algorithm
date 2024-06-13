def solution(data, ext, val_ext, sort_by):
    answer = [[]]
    index = {"code":0, "date":1, "maximum":2, "remain":3}
    newData = []
    for i in range(len(data)) :
        if data[i][index[ext]] < val_ext :
            newData.append(data[i])
    newData.sort(key=lambda x : x[index[sort_by]])
    answer = newData
    return answer