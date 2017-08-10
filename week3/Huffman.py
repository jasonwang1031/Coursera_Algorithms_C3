def read_from_file(filename):
    symbol_dict = {}
    # maps weights to a set of symbols under that cumulative weight
    # (starts as a set of one element each)
    weight_dict = {}
    weight_heap = [] # minimum heap of weights

    symbol = 1

    file = open(filename)
    for line in file.readlines():
        weight = int(line)
        symbol_dict[symbol] = "" # codes are initially empty
        addToMinHeap(weight_heap, weight)
        if weight not in weight_dict:
            weight_dict[weight] = set()
            weight_dict[weight].add(symbol)
        else:
            weight_dict[weight].add(symbol)
        symbol += 1

    return weight_dict, weight_heap, symbol_dict

def addToMinHeap(weight_heap, weight):
    # create a min-heap to store every symbol/weight 
    # Store the root in position 1
    # For any node in position i:
    # its left child (if any) is in position 2i
    # its right child (if any) is in position 2i + 1
    # its parent (if any) is in position i/2 

    weight_heap.append(weight) # Adds weight to the heap

    if len(weight_heap) <= 1: # If heap is only the root, return
        return

    num_index = len(weight_heap) - 1
    parent_index = (int((num_index + 1) / 2) - 1)

    while weight_heap[num_index] < weight_heap[parent_index] and num_index != 0:
        weight_heap[num_index], weight_heap[parent_index] = weight_heap[parent_index], weight_heap[num_index]
        num_index = parent_index
        parent_index = int((num_index + 1) / 2) - 1

def getRoot(heap):
    return heap[0]

def deleteMin(heap):
    """Deletes root from a minimum heap and returns value of the root"""

    # Swap root and last element
    temp = heap[0]
    heap[0] = heap[-1]
    heap[-1] = temp

    root = heap.pop()

    if len(heap) <= 1:
        return root

    num_index = 0

    if len(heap) < 3:
        # swap child and parent and return
        temp = heap[0]
        heap[0] = heap[1]
        heap[1] = temp
        return root

    child_index1 = 1
    child_index2 = 2

    while (heap[num_index] > heap[child_index1] or heap[num_index] > heap[child_index2]):
        if child_index2 >= len(heap):
            child_index = child_index1
        else:
            if heap[child_index1] < heap[child_index2]:
                child_index = child_index1
            elif heap[child_index2] < heap[child_index1]:
                child_index = child_index2

        temp = heap[num_index]
        heap[num_index] = heap[child_index]
        heap[child_index] = temp

        num_index = child_index
        child_index1 = (num_index + 1) * 2 - 1
        child_index2 = (num_index + 1) * 2

        if child_index1 >= len(heap):
            return root
        elif child_index2 >= len(heap):
            # first child exists but second does not;
            # only need to check the case when this child is not smaller than parent
            if heap[num_index] < heap[child_index1]:
                return root
    return root

def huffman_encode(weight_dict, weight_heap, symbol_dict):
    """Given a list of weights as a minimum heap and a dictionary mapping
    the weights (frequencies) to the symbol, returns a dictionary mapping
    the code to the original symbol"""

    while len(weight_heap) > 1:

        first_min_weight = deleteMin(weight_heap)
        second_min_weight = deleteMin(weight_heap)

        first_set = weight_dict[first_min_weight]
        second_set = weight_dict[second_min_weight]

        # looping over all symbols under a subtree of weight first_min_weight
        # and updating the mapping of symbol to code
        for e in first_set:
            symbol = symbol_dict[e]
            symbol_dict[e] = "0" + symbol # new code

        for e in second_set:
            symbol = symbol_dict[e]
            symbol_dict[e] = "1" + symbol

        new_weight = first_min_weight + second_min_weight
        # update heap of weights with new combined weight
        addToMinHeap(weight_heap, new_weight)

        # update weight-to-symbol dictionary by removing mapping of previous
        # weights and adding mapping of new weight to combined set of symbols
        # in the subtree of the new weight
        del weight_dict[first_min_weight]
        del weight_dict[second_min_weight]

        weight_dict[new_weight] = first_set.union(second_set)
        if len(weight_heap) <= 1:
            break # end looop if we combined the last two items in heap

    return

def main(filename):
    weight_dict, weight_heap, symbol_dict = read_from_file(filename)
    huffman_encode(weight_dict, weight_heap, symbol_dict)
    print (weight_dict)
    print (weight_heap)
    print (symbol_dict)

    max_size_code = 0
    min_size_code = 0

    for code in symbol_dict.values():
        if max_size_code == 0:
            max_size_code = len(code)
        if min_size_code == 0:
            min_size_code = len(code)
        if len(code) > max_size_code:
            max_size_code = len(code)
        if len(code) < min_size_code:
            min_size_code = len(code)

    print ("Maximum length of a code is: ", max_size_code)
    print ("Minimum length of a code is: ", min_size_code)



main("huffman.txt")