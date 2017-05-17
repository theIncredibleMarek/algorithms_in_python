#!/usr/bin/env python3

# TODO - start from the 2nd element - index is 1
# if ascending - check if smaller than the one immediately preceding
# if descending - check if bigger than the one immediately preceding
# finish when you reach the end of the list


def sort(input, ascending=True):
    print("Original: {}".format(input))
    print("Ascending sort: {}".format(ascending))
    # empty and one item lists are considered sorted
    if((len(input)) <= 1):
        return input

    passes = 0
    for index in range(1, len(input)):
        # no point in checking the first[0] item, that one is in order already
        target_index = 0
        if(ascending):
            first = input[index - 1]
            second = input[index]
        else:
            first = input[index]
            second = input[index - 1]

        if(first > second):
            # value is not at the correct place
            target = input[index]
            if index == 1:
                # if index is 1 then we just automatically swap the values - no
                # need for a for loop
                shift(input, 0, index)
            else:
                # start a loop to find out the target_index
                for i in range(index - 1, 0 - 1, -1):
                    # 0-1 is there because 0 index must be reached
                    if ascending:
                        if target >= input[i]:
                            target_index = i + 1
                            break
                    else:
                        if target <= input[i]:
                            target_index = i + 1
                            break
                shift(input, target_index, index)
        passes += 1

    print("{} passes".format(passes))
    return input


def shift(input, start_index, finish_index):
    # it's safe to assume that the number we want to move to the beginning of
    # the list(start_index) is at the end of it(finish_index)
    target = input[finish_index]
    for i in range(finish_index - 1, start_index - 1, -1):
        # since the target is already saved, I will just move all the items
        # below it one place forward
        input[i + 1] = input[i]
    input[start_index] = target


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
