"""
advent of code day 9

challenge number 1

find the first number in the list (after the preamble)
which is not the sum of two of the 25 numbers before it.
What is the first number that does not have this property?


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
    range_num = list(range(0,len(list_int)-1)) #since I +1
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
    last_item = len(all_number_list) #maybe plus 1?
    bad_num = -1
    while current_item < last_item:
    #    equal_num = False
        range_of_nums = list(range(current_item - len_preamble -1,current_item))
        number_list = []
        for num in range_of_nums:
            # create the list of values
            number_list.append(all_number_list[num])
        good_number = checksum(number_list)
        if good_number == False:
                bad_num = number_list[-1]
                return bad_num #current iteration is the bad #
        current_item = current_item + 1
    return bad_num



def runinstructions(all_instructions_list):
    """
    runinstructions

    takes a instruction list (all_instructions_list)
    runs through them (acc, jmp, nop)
    returns:
        the accumulator value (int return value)
        the last run instruction (int current_instruction)
    """
    return_value = 0
    instruction_tracker = [0] * len(all_instructions_list)
    second_call = False #was an instruction called twice
    current_instruction = 0
    while not second_call and current_instruction < len(all_instructions_list):
        if instruction_tracker[current_instruction] == 0: #first call
            instruction_tracker[current_instruction] = 1 #its called
            if all_instructions_list[current_instruction][0] == 'nop':
                current_instruction = current_instruction + 1
            elif all_instructions_list[current_instruction][0] == 'jmp':
                current_instruction = current_instruction + all_instructions_list[current_instruction][1]
            elif all_instructions_list[current_instruction][0] == 'acc':
                return_value = return_value + all_instructions_list[current_instruction][1]
                current_instruction = current_instruction + 1
        else:
            second_call = True
    return [return_value, current_instruction]


def parselines(all_lines):
    """
    parselines
    takes as input a list of strings (all_lines)
    returns a list of numbers (int)
    that contains all the lines
    """
    all_nums_list = []
    current_num = 0
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

#    instruction_return = runinstructions(boot_code)
#    acc_value = instruction_return[0]
#    instruction_return = findbadinstruction(boot_code)
    msg = 'Abad number: ' + str(bad_number)
    print(msg)
#    msg = 'Accumulator value full run: ' + str(instruction_return[0])
#    print(msg)
#    print(instruction_return[1])


#call the main function
main()
