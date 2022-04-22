def my_solution(bridge_length, weight, truck_weights):   
    
    answer = 0       
    
    on_bridge_truck = []
    time_list = []
    
    for idx in range(len(truck_weights)) :       
        
        if len(time_list) > 0 :
            time_list = list(map(lambda x:x - 1, time_list))
            if time_list[0] == 0 :
                time_list.pop(0)
                on_bridge_truck.pop(0)
            
        if sum(on_bridge_truck) + truck_weights[idx] > weight :    
            while sum(on_bridge_truck) + truck_weights[idx] > weight :
                del_time = time_list.pop(0)
                on_bridge_truck.pop(0)
                time_list = list(map(lambda x:x - del_time, time_list))
                answer += del_time
            
        on_bridge_truck.append(truck_weights[idx])
        time_list.append(bridge_length)
        answer += 1     
    
    answer += time_list[-1]
    
    return answer
'''
나름 잘 푼듯??
'''

if __name__ == "__main__" :
    
    bridge_length = 2
    weight = 10
    truck_weights = [7, 4, 5, 6]
    
    print(my_solution(bridge_length, weight, truck_weights))