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
MAX_ROWS = 128 #0-127
ROW_CHARS = 7
MAX_SEATS = 8 #0-7
SEAT_CHARS = 3
FILE_NAME = "day5_input.txt"




##################################
#
#  main
#
###################################
def main():
    with  open(FILE_NAME, 'r') as reader:
        all_lines = reader.read().splitlines()
    reader.close

    # loop through the lines
    current_line = 0
    number_high = 0
    same_line = False #start with appending a record (the set is blank when we start)
    for line in all_lines:
        #get all the multi-line stuff into a set of lines that we actually want to work with
        if len(line) > 0: # this line has data on it
            print(line)
    msg = "top seat number passports " + str(number_high)
    print(msg)

#call the main function
main()
