#!/usr/bin/python3


def sort(input, ascending=True):
    print("Original: {}".format(input))
    print("Ascending sort: {}".format(ascending))
    # empty and one item lists are considered sorted
    if((len(input)) <= 1):
        return input

    unsorted = True
    end = len(input)
    passes = 0
    # no need to check the last one in the array, that one will be sorted when
    # we reach the second to last

    for i in range(0, end - 1):
        # the min or the max depending on what we are looking for
        target = input[i]
        index = i
        # inner loop will find the max or min value - no need to look at the
        # first item , start with the one immediately following
        for j in range(i + 1, end):
            if ascending:
                # we are looking for the smallest value
                if input[j] < target:
                    target = input[j]
                    index = j
            else:
                if input[j] > target:
                    target = input[j]
                    index = j
        if index != i:
            # swap the values
            holder = input[i]
            input[i] = target
            input[index] = holder

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
