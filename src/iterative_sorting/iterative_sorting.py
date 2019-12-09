# TO-DO: Complete the selection_sort() function below 
def selection_sort( arr ):
    # loop through n-1 elements
    for i in range(0, len(arr) - 1):
        cur_index = i
        smallest_index = cur_index
        # TO-DO: find next smallest element
        # (hint, can do in 3 loc) 




        # TO-DO: swap




    return arr


# TO-DO:  implement the Bubble Sort function below
def bubble_sort( arr ):
    for i in range(len(arr)):
        # checks boolean to see if swap has occurred
        swap = False
        for i in range(0, len(arr) - i - 1):
            if arr[i] > arr[i + 1]:
                swap = True
                # swap if current index > neighbor index
                arr[i], arr[i + 1] = arr[i + 1], arr[i]
        if swap == False:
            pass
    return arr

# STRETCH: implement the Count Sort function below
def count_sort( arr, maximum=-1 ):

    return arr


# # INSERTION SORT
# l = [5, 3, 1, 6]

# i = 1
# temp = 3 # this is the number we want to insert into the sorted 
#          # half on the left
# j = 1

# def insertion_sort(list):
#     # Separate the first element from the rest of the array
#     # Think about it as a sorted list of one element

#     # For all other indices, beginning with [1]:
#     for i in range(1, len(l)):
#         # a. Copy the item at that index into a temp variable
#         temp = list[i]
#         # b. Iterate to the left until you find the correct index in the
#         #    "sorted" part of the array
#         j = i
#         while j > 0 and temp < list[j - 1]:
#             # Shift items over to the right as you iterate
#             list[j] = list[j - 1]
#             j -= 1
#         # c. When the correct index is found, copy temp into this pos  
#         list[j] = temp
#     return list