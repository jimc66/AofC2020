"""
advent of code day 12

challenge number 2
Actions
N
S
E
W
move waypoint by that many units
waypoint starts 10 units east and 1 unit north

L means to rotate the waypoint around the ship left (counter-clockwise) the given number of degrees.

R means to rotate the waypoint around the ship right (clockwise) the given number of degrees.


F means to move forward to the waypoint a number of times equal to the given value.
reminder:
North 0
East 90
South 180
West 270



"""
#import copy
import math
# "Globals"
FILE_NAME = "day12_input.txt"
#FILE_NAME = "testinput_12.txt"



def rotate(origin, point, angle):
    """
    rotate
    well... this is what the internet says to do to rotate

    I didn't know math would be involved!

    origin {x,y}
    point {x,y}
    angle math.radians(#)
    from: https://stackoverflow.com/a/34374437
    """
    or_x, or_y = origin
    p_x, p_y = point
    q_x = or_x + math.cos(angle) * (p_x - or_x) - math.sin(angle) * (p_y - or_y)
    q_y = or_y + math.sin(angle) * (p_x - or_x) + math.cos(angle) * (p_y - or_y)
    return int(round(q_x)), int(round(q_y))


def navigate(item, wayp_x, wayp_y, ship_x, ship_y):
    """
    navigate
    takes a list [0] char [1]int
    navigate based on the item

    returns
    way_x
    way_y
    sh_x
    sh_y

    """
    way_x = wayp_x
    way_y = wayp_y
    sh_x = ship_x
    sh_y = ship_y
    if item[0] == 'S':
        way_y -= item[1]
    elif item[0] == 'N':
        way_y += item[1]
    elif item[0] == 'E':
        way_x += item[1]
    elif item[0] == 'W':
        way_x -= item[1]
    elif item[0] == 'R' or item[0] == 'L':
        if item[0] == 'R':
            angle = -item[1]
        elif item[0] == 'L':
            angle = item[1]
        way_x, way_y = rotate((0, 0), (way_x, way_y), math.radians(angle))
    # forward and reverse
    elif item[0] == 'F':
        move_mult = item[1]
        xmove = move_mult * wayp_x
        ymove = move_mult * wayp_y
        sh_x = sh_x + xmove
        sh_y = sh_y + ymove
    return [way_x, way_y, sh_x, sh_y]

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
    #0-North 90-East 180-South 270-West
    ship_x_pos = 0 #x is east west
    ship_y_pos = 0 # y north south
    wayp_x_pos = 10 # x is east west
    wayp_y_pos = 1 #Y in North south

#    master_seat_list = []
##    new_seat_list = []
    master_dir_list = parselines(all_lines)
#    an_item = []
    for an_item in master_dir_list:
        wayp_x_pos, wayp_y_pos, ship_x_pos, ship_y_pos = navigate(an_item, wayp_x_pos, wayp_y_pos,
                                                                  ship_x_pos, ship_y_pos)
    msg = "North South: " + str(ship_x_pos)
    print(msg)
    msg = "East West: " + str(ship_x_pos)
    print(msg)
    man_dist = abs(ship_y_pos) + abs(ship_x_pos)
    msg = 'Manhattan Distance: ' + str(man_dist)
    print(msg)
#    msg = 'Final seatlist'
#    print(msg)
#    for alist in new_seat_list:
#        print(alist)


#call the main function
main()
