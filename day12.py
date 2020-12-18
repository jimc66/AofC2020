"""
advent of code day 12

challenge number 1
Actions
N
S
E
W
move by that many units

L
R
turn that many degrees

F move forward in the direction you are facing that many units
reminder:
North 0
East 90
South 180
West 270

challenge number 2

"""
import copy
# "Globals"
#FILE_NAME = "day12_input.txt"
FILE_NAME = "testinput_12.txt"
CURRENT_DIR = 0
NORTH_SOUTH = 0
EAST_WEST = 0




def parselines(all_lines):
    """
    parselines
    takes as input a list of strings (all_lines)
    returns a list of arrays [0] char [1] int
    that contains all the lines character by character
    and line by line
    """
    all_lines_list = []
#    current_num = 0
    single_list = []
    for line in all_lines:
        if len(line) > 0: # this line has data on it
            line = line.strip()
            char_val = line[0]
            int_val = int(line[1:])
            single_list.append(char_val)
            single_list.append(int_val)
            all_lines_list.append(single_list.copy())
            single_list.clear()
    return all_lines_list


def main():
    """
    main module
    """
    with  open(FILE_NAME, 'r') as reader:
        all_lines = reader.read().splitlines()
    reader.close
#    master_seat_list = []
##    new_seat_list = []
    master_dir_list = parselines(all_lines)
    msg = 'msg : ' 
    print(msg)
#    msg = 'Final seatlist'
#    print(msg)
#    for alist in new_seat_list:
#        print(alist)


#call the main function
main()
