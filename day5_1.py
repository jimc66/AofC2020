"""
advent of code day 5 challenge number 1
"""
# day 5 challenge 1
#
#The first 7 characters will either be F or B; these specify exactly one of the 128
#rows on the plane (numbered 0 through 127). Each letter tells you which half of a
# region the given seat is in. Start with the whole list of rows; the first letter
# indicates whether the seat is in the front (0 through 63) or the back (64 through 127).
#  The next letter indicates which half of that region the seat is in, and so on until
#  you're left with exactly one row.
# whole range  0 through 127
#
#The last three characters will be either L or R; these specify exactly one of the
#  8 columns of seats on the plane (numbered 0 through 7). The same process as above
#  proceeds again, this time with only three steps. L means to keep the lower half,
#  while R means to keep the upper half.
# Start by considering the whole range, columns 0 through 7.

# "Globals"
MAX_ROWS = 127 #0-127 - so actually 128
ROW_CHARS = 7
ROW_LOW = 'F'
ROW_HIGH = 'B'
MAX_SEATS = 7 #0-7 so actually 8
SEAT_CHARS = 3
SEAT_LOW = 'L'
SEAT_HIGH = 'R'
FILE_NAME = "day5_input.txt"

######
# findloc
# function to find which location
# pass in the string to check, return the row
# params:
# rowstring, the low and high values, the character for low, the character for high
######
def findloc(in_string, low, high, lowchar, highchar):
    """
    find the row that the seat is in
    """
    low_num = low #start at zero  ?
    # there is some kind of math problem here... something around
    high_num = high
    for iteration in range(len(in_string)-1):
        delta = high_num - low_num + 1
        if in_string[iteration] == lowchar:
            high_num = high_num - (delta / 2)
        elif in_string[iteration] == highchar:
            low_num = low_num + (delta / 2)
    if in_string[-1] == lowchar:
        return low_num
    elif in_string[iteration] == highchar:
        return high_num
    else:
        return -1


##################################
#
#  main
#
###################################
def main():
    """
    main module
    """
    with  open(FILE_NAME, 'r') as reader:
        all_lines = reader.read().splitlines()
    reader.close
    high_seat_id = 0
#    tester = 'BBFFBBFRLL'
#    row = findloc(tester[0:ROW_CHARS], 0, MAX_ROWS, ROW_LOW, ROW_HIGH)
#    seat = findloc(tester[ROW_CHARS:ROW_CHARS+SEAT_CHARS], 0, MAX_SEATS, SEAT_LOW, SEAT_HIGH)
#    seat_id = (row * 8) + seat
    # loop through the lines
    for line in all_lines:
        #get all the multi-line stuff into a set of lines that we actually want to work with
        if len(line) == ROW_CHARS + SEAT_CHARS: # this line has data on it
            row = findloc(line[0:ROW_CHARS], 0, MAX_ROWS, ROW_LOW, ROW_HIGH)
            seat = findloc(line[ROW_CHARS:ROW_CHARS+SEAT_CHARS], 0, MAX_SEATS, SEAT_LOW, SEAT_HIGH)
            seat_id = (row * 8) + seat
            if seat_id > high_seat_id:
                high_seat_id = seat_id

    msg = "top seat number: " + str(high_seat_id)
    print(msg)

#call the main function
main()
