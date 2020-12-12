"""
advent of code day 8 challenge number 1

acc increases or decreases a single global value called the accumulator by
the value given in the argument. For example, acc +7 would increase the
accumulator by 7. The accumulator starts at 0. After an acc instruction,
the instruction immediately below it is executed next.

jmp jumps to a new instruction relative to itself. The next instruction
to execute is found using the argument as an offset from the jmp instruction;
for example, jmp +2 would skip the next instruction, jmp +1

nop stands for No OPeration - it does nothing. The instruction
immediately below it is executed next.

Run your copy of the boot code.
Immediately before any instruction is executed a second time,
what value is in the accumulator?

"""

# "Globals"
FILE_NAME = "day8_input.txt"
#FILE_NAME = "testinput_8.txt"


def removebag(bagstr):
    """
    removebag

    takes a string (bagstr)
    removes the trailing
    ' bag' or ' bags'
    returns a string
    """
    if bagstr[-4:] == ' bag':
        return bagstr[0:-4]
    if bagstr[-5:] == ' bags':
        return bagstr[0:-5]
    return bagstr #found no match


def runinstructions(all_instructions_list):
    """
    runinstructions

    takes a instruction list (all_instructions_list)
    runs through them (acc, jmp, nop)
    and returns the accumulator (int)
    """
    return_value = 0
    #initial instruction tracker-can only run once
    instruction_tracker = [0] * len(all_instructions_list)
    second_call = False #was an instruction called twice
    current_instruction = 0
    while not second_call:
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
    return return_value


def parsecode(all_instructions):
    """
    parsecode
    takes as input a list of strings (AllInstructions)
    returns a list of instructions (string) and offsets (int)
    that contains all the instructions
    """
    all_instructions_list = []
    current_instruction = 0
    for line in all_instructions:
        #split between instruction and offset
        if len(line) > 0: # this line has data on it
            splitter = line.split()
            instruction = splitter[0].strip()
            offset_str = splitter[1].strip()
            offset_int = int(offset_str)
            one_instruction = []
            one_instruction.append(instruction)
            one_instruction.append(offset_int)
            all_instructions_list.append(one_instruction)
            current_instruction = current_instruction + 1
    return all_instructions_list


def main():
    """
    main module
    """
    with  open(FILE_NAME, 'r') as reader:
        all_lines = reader.read().splitlines()
    reader.close
    boot_code = []
    acc_value = 0
    boot_code = parsecode(all_lines)
    acc_value = runinstructions(boot_code)
#    gold_ones = bagcontents(all_bag_entries, 'shiny gold')
#    for bag in gold_ones:
#        new_ones = findbag(all_bag_entries, bag)
#        for items in new_ones:
#            if not items in gold_ones:
#                gold_ones.append(items)
#    total_bags = len(gold_ones) -1 #subtract gold
    msg = 'Accumulator Value: ' + str(acc_value)
    print(msg)


#call the main function
main()
