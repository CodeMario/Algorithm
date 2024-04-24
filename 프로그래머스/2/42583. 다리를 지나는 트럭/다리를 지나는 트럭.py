def solution(bridge_length, weight, truck_weights):
    answer = 0
    bridge = [0] * bridge_length
    bridge_weight = 0
    while True :
        if truck_weights == [] :
            answer += bridge_length
            break
        else :
            answer += 1
            bridge_weight += truck_weights[0] - bridge[0]
            del bridge[0]
            bridge.append(truck_weights[0])
            if weight - bridge_weight < 0 :
                bridge_weight -= bridge[-1]
                bridge[-1] = 0
            else :
                del truck_weights[0]

    return answer