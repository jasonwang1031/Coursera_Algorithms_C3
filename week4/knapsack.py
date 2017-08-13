import time

def knapsack_optimal_value(value_list, weight_list, capacity):
    
    #create the 2D list
    best_values_list = []
    best_values_list.append([])

    for w in range(0, capacity + 1):
        best_values_list[0].append(0)

    for i in range(1, len(value_list) + 1):
        best_values_list.append([])

        for w in range(0, capacity + 1):
            if weight_list[i - 1] > w:
                best_values_list[i].append(best_values_list[i - 1][w])

            else:
                best_values_list[i].append( max(best_values_list[i - 1][w],
                                best_values_list[i - 1][w - weight_list[i - 1]]
                                + value_list[i - 1]))

    return best_values_list[-1][-1]


if __name__ == "__main__":
    value_list = [] 
    weight_list = [] 

    file = open("knapsack2.txt")
    for line in file.readlines():
        i = line.split()
        value_list.append(int(i[0]))
        weight_list.append(int(i[1]))
    capacity = value_list.pop(0)
    weight_list.pop(0)

    start = time.time()
    best_value = knapsack_optimal_value(value_list, weight_list, capacity)
    end = time.time()
    print (best_value)
    print(end-start)


