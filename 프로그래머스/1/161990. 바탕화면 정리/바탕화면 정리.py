def solution(wallpaper):
    answer = []
    nx = []
    ny = []
    for i in range(len(wallpaper)) :
        for j in range(len(wallpaper[i])) :
            if wallpaper[i][j] == '#' :
                nx.append(j)
                ny.append(i)
    answer = [min(ny),min(nx),max(ny)+1,max(nx)+1]
    return answer