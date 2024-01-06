# Binary Search in Python

# Function that takes a list and target parameter
# Variables: middle, start, end, steps
# Recursion or while loop to keep splitting data
# Increase the steps each time a split is done
# Conditions to track target position

def binary_search(list, element):
    middle = 0
    start = 0
    end = len(list)
    steps = 0

    while(start <= end):
        print("Step",steps,":",str(list[start:end+1]))

        steps = steps+1
        middle = (start + end) // 2

        if element == list[middle]:
            return middle
        if element < list[middle]: # <-- if the element is less than the middle part, list is updated to this part only
            end = middle -1
        else:
            start = middle +1 # <-- if the element is higher than the middle, list is updated to the 2nd part of the list

    return -1

my_list = [1,2,3,4,5,6,7,8,9]
target = 6

binary_search(my_list, target)
