def checkOverHealing(health, maxHealth) :
    if health > maxHealth :
        health = maxHealth
    return health

def solution(bandage, health, attacks):
    answer = 0
    maxHealth = health
    time = 0

    for i in attacks :
        health += ((((i[0]-time-1)//bandage[0])*bandage[2])+(bandage[1]*(i[0]-time-1)))
        health = checkOverHealing(health,maxHealth)
        health -= i[1]
        time = i[0]

        if health <= 0 :
            return -1
    answer = health
    return answer