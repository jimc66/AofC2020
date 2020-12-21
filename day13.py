"""
advent of code day 13

challenge number 1

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
import math
# "Globals"
#FILE_NAME = "day13_input.txt"
FILE_NAME = "testinput_13.txt"


def parselines(all_lines):
    """
    parselines
    takes as input a list of strings (all_lines)
    returns a list:
    first item len 0 is #minutes
    2nd item is list of ints for busses (x) removed
    but I'll expect we end up using that later
    """
    all_lines_list = []
#    current_num = 0
    single_list = []
    # get the first line
    count_x = 0
    first_line = all_lines[0]
    char_val = first_line.strip()
    int_val = int(char_val)
    single_list.append(int_val)
    all_lines_list.append(single_list.copy())
    single_list.clear()
    rest_of_items = all_lines[1].split(',')
    for item in rest_of_items:
        if item != 'x': # this line has data on it
            char_val = item.strip()
            int_val = int(char_val)
            single_list.append(int_val)
        else:
            count_x += 1 #increment x, expecting to need it for part 2
    all_lines_list.append(single_list.copy())
    return all_lines_list

def calc_wait_time(time_start, min_interval):
    """
    wait_time
    takes times_starts and the number as int
    
    returns the  number about the time_start 
    """
    # go above timestart by the whole interval
    max_time = time_start + min_interval
    # figure out what the floor division
    # I like the 2nd way better
#    whole_wait_units = math.floor(max_time / min_interval)
#    whole_wait_units = time_start // min_interval
#    tot_time = (whole_wait_units+1)*min_interval
#    waiter = tot_time - time_start

    wait_time_total = max_time % min_interval
    if wait_time_total > 0:
        wait_time_total = min_interval - wait_time_total
    print(wait_time_total)
    return wait_time_total

def main():
    """
    main module
    """
    bus = 0
    wait_time = 0
    start_time = 0
    with  open(FILE_NAME, 'r') as reader:
        all_lines = reader.read().splitlines()
    reader.close
    line_list = parselines(all_lines)
    start_time = int(line_list[0][0])
    bus_list = line_list[1]
    abus_wait = calc_wait_time(start_time, bus_list[0])
    best_bus = {}
    best_bus['bus_pos'] = 0
    best_bus['bus_wait'] = abus_wait
#    low_bus = line_list[1][0]
    for idex, abus in enumerate(bus_list):
       abus_wait = calc_wait_time(start_time, abus)
       if abus_wait < best_bus['bus_wait']:
           best_bus['bus_pos'] = idex
           best_bus['bus_wait'] = abus_wait
    bus = bus_list[best_bus['bus_pos']]
    msg = "bus: " + str(bus)
    print(msg)
    wait_time = best_bus['bus_wait']
    msg = "wait time: " + str(wait_time)
    print(msg)
    id_min = bus * wait_time
    msg = 'product: ' + str(id_min)
    print(msg)
#    msg = 'Final seatlist'
#    print(msg)
#    for alist in new_seat_list:
#        print(alist)


#call the main function
main()
