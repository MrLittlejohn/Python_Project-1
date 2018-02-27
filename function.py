# Littlejohn, sort functions for a python Project.
#Dr.Decker, Due: Feb 26th, 2018, class: 16:00 to 17:15

#All rights are reserved to me, the almighty.
#1st includes insertion sort
#2nd is the recursive binary sort
#3rd is the split sort

def insertion_sort(insertion_list) :
    for number in range(1,len(insertion_list)):         #start 1 over, as we dont compare the 1st element with anything
        current = insertion_list[number]
        position = number

        while position > 0 and insertion_list[position - 1] > current :
            insertion_list[position] = insertion_list[position - 1]
            position = position -1

        insertion_list[position] = current


def binary_search(binary_list, item, offset) :
    if not binary_list :
        return print(None)
    
    elif binary_list[len(binary_list) // 2] == item : # if when the binary list divides by 2 and it equals the item,
        return offset + len(binary_list) // 2         # return the offset added to the length of where the binary list is sitting 
    
    elif binary_list[len(binary_list) // 2] > item :                                # if when the binary list divides by 2, and the length number is greater than where the item is sitting,
        return binary_search(binary_list[:len(binary_list) // 2], item, offset)     # return the function, as it will do it over and over again until it finds the number, so pass everything through as it will be used again
                                                                                    # until the item equals the the first else if statement.
                                                                                    # Also, make sure to only exclude the right half of the length of the list, otherwise it will go infinitely, and reveive an error
    else :
        return binary_search(binary_list[(len(binary_list) // 2) + 1:], item, offset+(len(binary_list) // 2) + 1)   #if all else fails, it must be on the right half, so call the function again recursively
                                                                                                                    #the purpose for adding 1, is incase there are an even amount of numbers in the list.
                                                                                                                    #by adding 1, you prevent a number from being ignore


def split_char(string, char) :

    if char in string :                     #make sure the character, or symbol is actually in the string
        temp = 0
        while temp < len(string) :              #as long as the temporary variable is less than the length of the string,
            if string[temp] == char[0] :        #if the string equals the character, make the position whatever the temp may/not be
                position = temp
                break
            temp += 1

        before_split = string[:position]        #grab everything before the seperator

        after_split = split_char(string[position + 1:], char) #grab everything after the split, recursively.

        after_split = [before_split] + after_split[:]   

        return after_split

    else :
        return [string]

        
    
