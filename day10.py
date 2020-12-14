"""
advent of code day 10

challenge number 1

take the adapter list, find the jolt differences
in order (1 jolt, 3 jolt)
What is the number of 1-jolt differences multiplied by
the number of 3-jolt differences?

challenge number 2
What is the total number of distinct ways you can arrange
the adapters to connect the charging outlet to your device?

approach:
combinations from each postition


"""

# "Globals"
#FILE_NAME = "day10_input.txt"
#from os import O_APPEND
FILE_NAME = "testinput_10.txt"
LOW_DIF = 1
HIGH_DIF = 3
PATH_DICT = {}

def pathfinder(all_number_list, iterator):
    """
    pathfinder

    iterate through finding the path to the end
    from the current spot (iterator)
    for the list of numbers (all_number_list)

    add to global PATH_DICT
    also used global HIGH_DIF
    """
    if iterator == len(all_number_list) -1:
        return 1
    if iterator in PATH_DICT:
        return PATH_DICT[iterator] # so it doesn't run forever
    return_value = 0
    for looper in range(iterator + 1, len(all_number_list)):
        if all_number_list[looper] - all_number_list[iterator] <= HIGH_DIF:
            return_value += pathfinder(all_number_list, looper)
    PATH_DICT[iterator] = return_value
    return return_value



def find_number_dif(all_number_list, target_dif):
    """
    find_number_dif

    takes the number list as input (list of integers)
    and the target dif (int)
    runs through number list to counts the occurences
    of target dif and returns that (return_value) as int
    """
    return_value = 0
    current_listitem = 0
    last_item = len(all_number_list)
    while current_listitem < last_item-1:
        if all_number_list[current_listitem] + target_dif == all_number_list[current_listitem+1]:
            return_value += 1
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
    # sort from lowest to highest
    # add the "zero" adapter for charging outlet BEFORE you sort
    number_list.append(0)
    number_list.sort()
    # add the "built in adapter" of HIGH DIF AFTER you sort
    number_list.append(number_list[len(number_list)-1]+HIGH_DIF)
    print(number_list)
    low_difference = find_number_dif(number_list, LOW_DIF)
    high_difference = find_number_dif(number_list, HIGH_DIF)
    product_difference = low_difference * high_difference

    msg = 'Low Dif : ' + str(low_difference) + "  High Dif : " + str(high_difference)
    print(msg)
    msg = 'Product low * high : ' + str(product_difference)
    print(msg)
    total_paths = pathfinder(number_list, 0)
    msg = 'Total Paths: ' + str(total_paths)
    print(msg)


#call the main function
main()
