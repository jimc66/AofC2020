"""
advent of code day 9

challenge number 1

find the first number in the list (after the preamble)
which is not the sum of two of the 25 numbers before it.
What is the first number that does not have this property?


"""

# "Globals"
FILE_NAME = "day9_input.txt"
#FILE_NAME = "testinput_8.txt"

def findbadinstruction(all_instruction_list):
    """
    findbadinstruction
    takes the instruction list as input
    iterates through the list changing 1 instruction list
    one at a time (jmp --> nop) (nop --> jmp)
    until you run through to the end of the list

    returns the value of the accumulator (int)
    and the changed instruction as an FYI (string)
    """
    modification_str = ''
    current_instruction = 0
    original_instruction = []
    changed_instruction = []
    last_instruction = len(all_instruction_list)
    while current_instruction < last_instruction:
        original_instruction = all_instruction_list[current_instruction][:]
        changed_instruction = original_instruction[:] # double check: copy?
        if original_instruction[0] == 'nop':
            changed_instruction[0] = 'jmp'
            all_instruction_list[current_instruction] = changed_instruction
        elif original_instruction[0] == 'jmp':
            changed_instruction[0] = 'nop'
            all_instruction_list[current_instruction] = changed_instruction
        instruction_return = [0, 0]
        instruction_return = runinstructions(all_instruction_list)
        all_instruction_list[current_instruction] = original_instruction[:] #change back
        if instruction_return[1] == last_instruction: #made it to the end
            modification_str = 'changed line ' + str(current_instruction)
            return [instruction_return[0], modification_str]
        current_instruction = current_instruction + 1
    modification_str = 'error'
    return [-1, modification_str]


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
#    acc_value = 0
#    last_inst = 0
    instruction_return = [0, 0]
    number_list = parselines(all_lines)
#    instruction_return = runinstructions(boot_code)
#    acc_value = instruction_return[0]
#    instruction_return = findbadinstruction(boot_code)
#    msg = 'Accumulator Value on early exit: ' + str(acc_value)
#    print(msg)
#    msg = 'Accumulator value full run: ' + str(instruction_return[0])
#    print(msg)
#    print(instruction_return[1])


#call the main function
main()
