#!/usr/bin/env python3

import math

def sort(input, ascending=True):
    print("Original: {}".format(input))
    print("Ascending sort: {}".format(ascending))
    # empty and one item lists are considered sorted
    if((len(input)) <= 1):
        return input

    output =  mergesort(input, ascending)
    return output

def mergesort(input, ascending):
    length = len(input)
    if length <= 1:
        return input

    # split the input
    left = input[:math.ceil(length/2)]
    right = input[math.ceil(length/2):]

    # sort the left and the right sides
    left = mergesort(left, ascending)
    right = mergesort(right, ascending)

    #merge the sides together
    left_point = 0
    right_point = 0
    index = 0
    output = []
    while(left_point < len(left) and right_point < len(right)):
        if(ascending):
            value_1 = left[left_point]
            value_2 = right[right_point]
        else:
            value_1 = right[right_point]
            value_2 = left[left_point]
        if value_1 > value_2:
            output.append(right[right_point])
            right_point+=1
        else:
            output.append(left[left_point])
            left_point+=1
            
    if left_point == len(left):
        # use either += or list.extend()
        output += right[right_point:]
    if right_point == len(right):
        # extend unfolds the second list
        output.extend(left[left_point:])
    return output

print(sort([1, 2, 1], False))
print(sort([2, 1, 7, 3, 4, 5, 6, 2, 3, 1], False))
print(sort([1, 2, 3, 4, 5, 6], False))
print(sort([2], False))
print(sort([], False))

print(sort([2, 1]))
print(sort([1, 2, 1]))
print(sort([2, 1, 7, 3, 4, 5, 6, 2, 3, 1]))
print(sort([1, 2, 3, 4, 5, 6]))
print(sort([2]))
print(sort([]))
