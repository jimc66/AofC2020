"""
advent of code day 6 challenge number 1

The form asks a series of 26 yes-or-no questions marked a through z.
All you need to do is identify the questions for which anyone in your
group answers "yes".



For each group, count the number of questions
to which anyone answered "yes". What is the sum of those counts?

"""

# "Globals"

FILE_NAME = "day6_input.txt"

######
# getentries
# function to get the entries
# 
# params:
# 
######
def getentries(in_string):
    """
    this is just a shell from the last one...
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
    elif in_string[-1] == highchar:
        return high_num
    else:
        return -1


def main():
    """
    main module
    """
    with  open(FILE_NAME, 'r') as reader:
        all_lines = reader.read().splitlines()
    reader.close
    all_group_entires = [] #for the list of all the groups
    # loop through the lines
    for line in all_lines:
        #get all the multi-line stuff into a set of lines that we actually want to work with
        if len(line) == ROW_CHARS + SEAT_CHARS: # this line has data on it
            row = findloc(line[0:ROW_CHARS], 0, MAX_ROWS, ROW_LOW, ROW_HIGH)
            seat = findloc(line[ROW_CHARS:ROW_CHARS+SEAT_CHARS], 0, MAX_SEATS, SEAT_LOW, SEAT_HIGH)
            seat_id = (row * 8) + seat
            all_bording_passes.append(seat_id) #add the seat id / boarding pass to the list
            if seat_id > high_seat_id:
                high_seat_id = seat_id

    my_seat = findseat(all_bording_passes) # so we can figure out which one is ours
    msg = "my seat: " + str(my_seat)
    print(msg)

#call the main function
main()
