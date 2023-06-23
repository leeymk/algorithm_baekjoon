def solution(bridge_length, weight, truck_weights):
    answer = 0
    bridge = [0 for _ in range(bridge_length)]
    sum_bridge = 0
    
    while bridge:
        answer += 1
        t = bridge.pop(0)
        sum_bridge -= t
        if truck_weights:
            if sum_bridge + truck_weights[0] <= weight:
                sum_bridge = sum_bridge + truck_weights[0]
                truck = truck_weights.pop(0)
                bridge.append(truck)
            else:
                bridge.append(0)
                
    return answer
    