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
#import copy
# "Globals"
FILE_NAME = "day12_input.txt"
#FILE_NAME = "testinput_12.txt"
CURRENT_DIR = 90 #0-North 90-East 180-South 270-West
NORTH_SOUTH = 0
EAST_WEST = 0


def navigate(item):
    """
    navigate
    takes a list [0] char [1]int
    navigate based on the item
    modifies the globals
    CURRENT_DIR
    NORTH_SOUTH
    EAST_WEST
    """
    global CURRENT_DIR #0-North 90-East 180-South 270-West
    global NORTH_SOUTH 
    global EAST_WEST 
    if item[0] == 'S':
        NORTH_SOUTH -= item[1]
    elif item[0] == 'N':
        NORTH_SOUTH += item[1]
    elif item[0] == 'E':
        EAST_WEST += item[1]
    elif item[0] == 'W':
        EAST_WEST -= item[1]
    elif item[0] == 'R':
        CURRENT_DIR += item[1]
    elif item[0] == 'L':
        CURRENT_DIR -= item[1]        
    # forward and reverse
    elif item[0] == 'F' or item[0] == 'R':
        if item[0] == 'R':
            direction = -item[1] # see if this works or if its too clever
        else:
            direction = item[1]
        if CURRENT_DIR == 0:
            NORTH_SOUTH += direction
        elif CURRENT_DIR == 180:
            NORTH_SOUTH -= direction
        elif CURRENT_DIR == 90:
            EAST_WEST += direction
        elif CURRENT_DIR == 270:
            EAST_WEST -= direction
    if CURRENT_DIR >= 360:
        CURRENT_DIR -= 360
    elif CURRENT_DIR < 0:
        CURRENT_DIR += 360
    return

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
#    an_item = []
    for an_item in master_dir_list:
        navigate(an_item)
    msg = "North South: " + str(NORTH_SOUTH)
    print(msg)
    msg = "East West: " + str(EAST_WEST)
    print(msg)
    man_dist = abs(NORTH_SOUTH) + abs(EAST_WEST)
    msg = 'Manhattan Distance: ' + str(man_dist)
    print(msg)
#    msg = 'Final seatlist'
#    print(msg)
#    for alist in new_seat_list:
#        print(alist)


#call the main function
main()
