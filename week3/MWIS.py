def import_file(filename):

    weight_list = []
    mw_list = []

    file = open(filename)
    weight_list = [int(x) for x in file.readlines()]

    mw_list.append(weight_list[0])
    # maximum weight of MWIS at 1
    mw_list.append(max(weight_list[0], weight_list[1]))
    # maximum weight of MWIS at 2
    i = 2
    # for all the rest of the vertices, find maximum-weight of the MWIS at each
    # position corresponding to the given weight_list
    while i < len(weight_list):
        mw_list.append(max(mw_list[i - 1],
        mw_list[i - 2] + weight_list[i]))
        i += 1
    return weight_list,mw_list


def get_mwis(mw_list, weight_list):

    mwis_set = set()

    i = len(mw_list) - 1
    while i > 1:
        if i == 2 and mw_list[i - 1] >= (mw_list[i - 2] + weight_list[i]):
            if mw_list[0] >= mw_list[1]: mwis_set.add(1)
            else: mwis_set.add(2)

        elif i == 2 and mw_list[i - 1] < (mw_list[i - 2] + weight_list[i]):
            mwis_set.add(3) 
            mwis_set.add(1)
        elif i == 3 and mw_list[i - 1] >= (mw_list[i - 2] + weight_list[i]):
            i -= 1
        elif i == 3 and mw_list[i - 1] < (mw_list[i - 2] + weight_list[i]):

            if mw_list[1] >= (mw_list[0] + weight_list[2]):
                if mw_list[0] >= mw_list[1]:
                    mwis_set.add(1)
                else:
                    mwis_set.add(2)

            elif mw_list[1] < (mw_list[0] + weight_list[2]):
                # element at index 2 is in MWIS, add this and index 0 vertex
                mwis_set.add(3) # correct
                mwis_set.add(1)


        if mw_list[i - 1] >= (mw_list[i - 2] + weight_list[i]):
            i -= 1 # i-th element not in mw_set, just increment down one
        else:
            mwis_set.add(i + 1)
            # i-th element is in mw_set, add it and skip the next vertex
            i -= 2
    return mwis_set

def main(filename):
    weight_list, mw_list = import_file(filename)
    mw_set = get_mwis(mw_list, weight_list)
    print (mw_set)

main("mwis.txt")