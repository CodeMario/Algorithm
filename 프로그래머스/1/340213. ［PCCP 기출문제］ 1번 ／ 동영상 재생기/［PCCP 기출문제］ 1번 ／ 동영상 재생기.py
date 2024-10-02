def ChangeFormat(t) :
    t = int(t[:2])*60 + int(t[3:])
    return t

def solution(video_len, pos, op_start, op_end, commands):
    answer = ''
    video_len = ChangeFormat(video_len)
    pos = ChangeFormat(pos)
    op_start = ChangeFormat(op_start)
    op_end = ChangeFormat(op_end)
    
    if op_start <= pos <= op_end :
        pos = op_end
    
    for i in commands :
        if i == 'prev' :
            pos -= 10
            if pos < 0 :
                pos = 0
                
        elif i == 'next' :
            pos += 10
            if pos > video_len :
                pos = video_len
        
        if op_start <= pos <= op_end :
            pos = op_end
    mm,ss = pos//60,pos%60
    answer = f'{mm:0>2}'+':'+f'{ss:0>2}'
    return answer