#!/usr/bin/env python3


def sort(input, ascending=True):
    print("Original: {}".format(input))
    print("Ascending sort: {}".format(ascending))
    # empty and one item lists are considered sorted
    if((len(input)) <= 1):
        return input

    unsorted = True
    sorted_limit = len(input) - 1
    passes = 0
    while(unsorted):
        unsorted = False
        for i in range(sorted_limit):
            if(ascending):
                first = input[i]
                second = input[i + 1]
            else:
                first = input[i + 1]
                second = input[i]

            if(first > second):
                # swap the values
                unsorted = True
                if(ascending):
                    input[i + 1] = first
                    input[i] = second
                else:
                    input[i + 1] = second
                    input[i] = first

        # because the end of the list is now sorted we don't have to compare it
        # anymore
        sorted_limit -= 1
        if(sorted_limit <= 1):
            unsorted = False
        passes += 1

    print("{} passes".format(passes))
    return input


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
