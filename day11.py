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


"""

# "Globals"
FILE_NAME = "day11_input.txt"
#FILE_NAME = "testinput_11.txt"


def seatok(all_seat_list, seat):
    """
    seatok

    takes all_seat_list as input

    figure out if the seat is
    occupied and good to stay occupied
    occupied and should be freed up
    free and should be occupied
    returns 
    True no change / seat OK (free or not)
    False seat needs to change
    """
    return_value = True
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
    current_listitem = 0
    last_item = len(all_seat_list)
    while current_listitem < last_item-1:
#        if all_number_list[current_listitem] + target_dif == all_number_list[current_listitem+1]:
##            return_value += 1
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
    current_listitem = 0
    last_item = len(all_seat_list)
    while current_listitem < last_item-1:
#        if all_number_list[current_listitem] + target_dif == all_number_list[current_listitem+1]:
##            return_value += 1
        current_listitem += 1 #increment by 1
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
    for line in all_lines:
        if len(line) > 0: # this line has data on it
#            string_int = int(line)
#            all_nums_list.append(string_int)
            print('hello')
    return all_lines_list


def main():
    """
    main module
    """
    with  open(FILE_NAME, 'r') as reader:
        all_lines = reader.read().splitlines()
    reader.close
    seat_list = []
    new_seat_list = []
    seat_list = parselines(all_lines)
    while new_seat_list != seat_list:
        new_seat_list = seat_list.copy()
        seat_list = check_all_seats(new_seat_list)
    occ_seats = count_seats(new_seat_list)
    msg = 'Occupied Seats : ' + str(occ_seats)
    print(msg)


#call the main function
main()
