"""
advent of code day 9

challenge number 1

find the first number in the list (after the preamble)
which is not the sum of two of the 25 numbers before it.
What is the first number that does not have this property?

challenge number 2

take the number from challenge 1
find the set of contiguous numbers that sum to this number
then add the smallest and largest number in this set
"""

# "Globals"
FILE_NAME = "day9_input.txt"
#from os import O_APPEND
#FILE_NAME = "testinput_9.txt"
PREAMBLE_LEN = 25

def checksum(list_int):
    """
    checksum
    see if any of the numbers in the list
    when added together equal the last number
    returns True if this is the case
    False if no 2 numbers equal the last
    """
    return_value = False
    target_sum = list_int[len(list_int)-1]
    range_num = list(range(0, len(list_int)-1)) #since I +1
    number_list = []
    for num in range_num:
        # create the list of values
        number_list.append(list_int[num])
    for first in range_num:
        for second in range_num:
            if not second == first:
                if number_list[first] + number_list[second] == target_sum:
                    return_value = True
                    return return_value
    return return_value


def findbadnum(all_number_list, len_preamble):
    """
    findbadnum
    takes the number list as input (list of integers)
    iterates through the list starting AFTER the preamble
    one at at time checks to see if the number is a sum of
    2 numbers in the preceding (preamble) numbers

    returns the the number that is not (int)
    or a negative 1 if not found
    """
    current_item = len_preamble + 1
    last_item = len(all_number_list)
    bad_num = -1
    while current_item < last_item:
    #    equal_num = False
        range_of_nums = list(range(current_item - len_preamble -1, current_item))
        number_list = []
        for num in range_of_nums:
            # create the list of values
            number_list.append(all_number_list[num])
        good_number = checksum(number_list)
        if not good_number:
            bad_num = number_list[-1]
            return bad_num #current iteration is the bad #
        current_item = current_item + 1
    return bad_num

def bigandsmall(number_list, start, end):
    """
    bigandsmall
    take a list of numbers, a start and end of range)
    return the sum of the smallest and larget
    """
    # start with the first number being the lowest and highest
    lowest = number_list[start]
    highest = number_list[start]
    for iterate in range(start, end):
        if number_list[iterate] < lowest:
            lowest = number_list[iterate]
        if number_list[iterate] > highest:
            highest = number_list[iterate]
    ret_value = lowest + highest
    return ret_value


def find_number_list(all_number_list, target_sum):
    """
    find_number_list

    takes the number list as input (list of integers)
    and the target_sum (int)
    runs through number list to find the range that equals
    the target sum. Adds the first and last value in that
    list and return that (return_value) as int

    returns:
        the accumulator value (int return value)
        the last run instruction (int current_instruction)
    """
    return_value = 0
    current_listitem = 0
    last_item = len(all_number_list)
    while current_listitem < last_item:
        list_sum = 0
#        list_end = 0
        iterator = current_listitem + 1 
        number_list = list(range(current_listitem, last_item))
        for iterator in number_list:
            list_sum = list_sum + all_number_list[iterator]
            if list_sum == target_sum:
                return_value = bigandsmall(all_number_list, current_listitem, iterator)
                return return_value
            elif list_sum > target_sum:
                break #we're over the total, go to the next num
        current_listitem += 1 #increment by 1
    return return_value


def parselines(all_lines):
    """
    parselines
    takes as input a list of strings (all_lines)
    returns a list of numbers (int)
    that contains all the lines
    """
    all_nums_list = []
#    current_num = 0
    for line in all_lines:
        if len(line) > 0: # this line has data on it
            string_int = int(line)
            all_nums_list.append(string_int)
    return all_nums_list


def main():
    """
    main module
    """
    with  open(FILE_NAME, 'r') as reader:
        all_lines = reader.read().splitlines()
    reader.close
    number_list = []
    number_list = parselines(all_lines)
    bad_number = findbadnum(number_list, PREAMBLE_LEN)
    find_list_ret = find_number_list(number_list, bad_number)
    msg = 'Abad number: ' + str(bad_number)
    print(msg)
    msg = 'The total of the first and last in range: ' + str(find_list_ret)
#    msg = 'Accumulator value full run: ' + str(instruction_return[0])
    print(msg)
#    print(instruction_return[1])


#call the main function
main()
