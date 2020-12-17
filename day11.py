"""
advent of code day 11

challenge number 1

he seat layout fits neatly on a grid.
Each position is either
floor (.)
an empty seat (L)
an occupied seat (#)

All decisions are based on the number of occupied seats adjacent
to a given seat (one of the eight positions immediately
up, down, left, right, or diagonal from the seat).
The following rules are applied to every seat simultaneously:

If a seat is empty (L) and there are no occupied seats adjacent to it,
the seat becomes occupied.
If a seat is occupied (#) and four or more seats adjacent to it are also occupied
the seat becomes empty.
Otherwise, the seat's state does not change.


challenge number 2
new visibility method
instead of considering just the eight immediately adjacent seats,
consider the first seat in each of those eight directions even if it
extends beyond adjacent seats

the rule change for occupied seats becoming empty after 5 or more

"""
import copy
# "Globals"
#FILE_NAME = "day11_input.txt"
FILE_NAME = "testinput_11.txt"
OCC_SEAT = '#'
EMPTY_SEAT = 'L'
FLOOR = '.'

def seats_searcher(all_seat_list, seatrow, seatcol, rowinc, colinc):
    """
    starts at current seat and searches for the first seat
    (OCC_SEAT or EMPTY_SEAT), starting in seatrow, seatcol
    and extending out in the direction of the row increment
    (rowinc) and column increment (colinc) until a seat is found
    or the boundaries all all_seat_list are reached
    note rowinc or colinc may be pos, negative, or zero
    returns the seat value as a char
    if there is no seat found, returns FLOOR

    this needs to be looked at:
    the inputs i think are right
    but there is something wrong with:
    where the loops start - there is a lot of logic
    but still when on same row there is an issue with starting
    on the wrong item, look at it when you have better focus
    """
    found_seat = FLOOR #default return
    #figure out the row boundaries
    if rowinc < 0:
        seatrowend = -1 #see if this is off
    elif rowinc == 0:
        seatrowend = seatrow + 1 #to allow to loop once
    else:
        seatrowend = len(all_seat_list) -1 #check for off by one
    #figure out the column boundaries
    if colinc < 0:
        seatcolend = 0 #see if this is off
    elif colinc == 0:
        seatcolend = seatcol + 1 #to allow to loop once / no increment as we are checking the row
    else:
        seatcolend = len(all_seat_list[seatrow]) - 1
    if rowinc == 0:
        rowinc = 1 #so it loops one time for staying on same row
    if colinc == 0:
        colinc = 1 #col loop one time too
    for row in range(seatrow + rowinc, seatrowend, rowinc): #skip the seat you are in with the +rowinc
        for col in range(seatcol + colinc, seatcolend, colinc): #skip the seat you are in +colinc
            if all_seat_list[row][col] == OCC_SEAT:
                found_seat = OCC_SEAT
                return found_seat
            elif all_seat_list[row][col] == EMPTY_SEAT:
                found_seat = EMPTY_SEAT
                return found_seat
                # if you keep finding floor, roll through to the end
    return found_seat

def seatok(all_seat_list, seatrow, seatcol):
    """
    seatok

    takes all_seat_list
    seatrow and seatcol within row
    as input

    figure out if the seat is
    occupied and good to stay occupied
    occupied and should be freed up
    free and should be occupied
    returns
    True no change / seat OK (free or not)
    False seat needs to change
    """
    return_value = True
    if all_seat_list[seatrow][seatcol] == FLOOR:
        return True
    occ_seats = 0
    list_of_seats = []
    counter = 0
    for rowdir in (-1, 0, 1):
        for coldir in (-1, 0, 1):
            list_of_seats.append(seats_searcher(all_seat_list, seatrow, seatcol, rowdir, coldir))
            counter += 1
    occ_seats = list_of_seats.count(OCC_SEAT)

    # now that we have a count of occupied seats, figure out what to do
    if all_seat_list[seatrow][seatcol] == OCC_SEAT:
        if occ_seats > 5: # including the current seat
            return_value = False
    else: #not occupied
        if occ_seats == 0: #all adjacent also empty
            return_value = False
    return return_value



def check_all_seats(all_seat_list):
    """
    check_all_seats

    takes the seat list as input
    and runs through list and changes the seats as needed
    returns an updated seat list
    with any required changes (which might be none)
    """
    return_value = []
    return_value = copy.deepcopy(all_seat_list) # for now
    current_listitem = 0
    last_item = len(all_seat_list)
    while current_listitem < last_item:
        for col_iterator in range(len(all_seat_list[current_listitem])):
            if not seatok(all_seat_list, current_listitem, col_iterator):
                # flip the seat if "not ok"
                if all_seat_list[current_listitem][col_iterator] == OCC_SEAT:
                    return_value[current_listitem][col_iterator] = EMPTY_SEAT
                else:
                    return_value[current_listitem][col_iterator] = OCC_SEAT
        current_listitem += 1 #increment by 1
    return return_value


def count_seats(all_seat_list):
    """
    count_seats

    takes the seat list as input
    and runs through list and counts the occupied seats
    returns occupied seats as int
    """
    return_value = 0
    for one_list in all_seat_list:
        return_value += one_list.count(OCC_SEAT)
    return return_value


def parselines(all_lines):
    """
    parselines
    takes as input a list of strings (all_lines)
    returns a list of char arrays
    that contains all the lines character by character
    and line by line
    """
    all_lines_list = []
#    current_num = 0
    single_line = []
    for line in all_lines:
        if len(line) > 0: # this line has data on it
            single_line = list(line)
            all_lines_list.append(single_line)
            single_line.clear()
    return all_lines_list


def main():
    """
    main module
    """
    with  open(FILE_NAME, 'r') as reader:
        all_lines = reader.read().splitlines()
    reader.close
    master_seat_list = []
    new_seat_list = []
    master_seat_list = parselines(all_lines)
    new_seat_list = copy.deepcopy(master_seat_list)
    new_seat_list = check_all_seats(new_seat_list)
    while new_seat_list != master_seat_list:
        #update the master list to the new list of seats
        master_seat_list = copy.deepcopy(new_seat_list)
        new_seat_list = check_all_seats(new_seat_list)
    occ_seats = count_seats(new_seat_list)
    msg = 'Occupied Seats : ' + str(occ_seats)
    print(msg)
#    msg = 'Final seatlist'
#    print(msg)
#    for alist in new_seat_list:
#        print(alist)


#call the main function
main()
