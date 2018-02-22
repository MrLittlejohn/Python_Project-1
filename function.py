def insertion_sort(insertion_list) :
    for number in range(1,len(insertion_list)):
        current = insertion_list[number]
        position = number

        while position > 0 and insertion_list[position - 1] > current:
            insertion_list[position] = insertion_list[position - 1]
            position = position -1

        insertion_list[position] = current

        
        
