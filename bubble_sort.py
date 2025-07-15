
def bubble_sort(list):
    for i in range(len(list)):

        for l in range(len(list) - 1):
            if list[l] > list[l+1]:
                
                list[l], list[l+1] = list[l+1], list[l]

    return list