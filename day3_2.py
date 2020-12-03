# day 2 challenge 2
# Starting at the top-left corner of your map and following a slope of:
#  
#    Right 1, down 1.
#    Right 3, down 1. (This is the slope you already checked.)
#    Right 5, down 1.
#    Right 7, down 1.
#    Right 1, down 2.
# how many trees would you encounter? 
#What do you get if you multiply together the number of trees encountered on each of the listed slopes?

max_right=7 #for bulking out the array
x_moves=[1,3,5,7,1]
y_moves=[1,1,1,1,2]

number_good=[0,0,0,0,0]
number_bad=[0,0,0,0,0]
file_name="day3_input.txt"
curr_pos=[0,0]
x_move=3
y_move=1
tree_char="#"
clear_char="."

with  open(file_name, 'r') as reader:
    all_lines=reader.read().splitlines()
tot_lines = len(all_lines)-1
reader.close
# figure out how "wide" the strings need to be
line_length=len(all_lines[0])
length_needed=tot_lines * max_right
times_to_repeat = (length_needed // line_length) +1

# and make the strings the right "width"
current_line=0
for line in all_lines:
    print (line)
    line = line * times_to_repeat
    all_lines[current_line]=line
    new_len=len(line)
    current_line=current_line+1

#now make our way "down" the file
tot_times_to_repeat = len(x_moves)
current_iteration=0
looper=0
while looper <tot_times_to_repeat:
    looper=looper+1
    y_pos=0
    x_pos=0
    y_move=y_moves[current_iteration]
    x_move=x_moves[current_iteration]
    number_bad[current_iteration]=0
    number_good[current_iteration]=0
    while y_pos <tot_lines:
        y_pos=y_pos+y_move
        x_pos=x_pos+x_move
        pos_char= all_lines[y_pos][x_pos]
        if pos_char == tree_char:
            number_bad[current_iteration]=number_bad[current_iteration]+1
        else:
            number_good[current_iteration]=number_good[current_iteration]+1
    current_iteration=current_iteration+1

looper=2
product =number_bad[0] * number_bad[1] # have to start somewhere
while looper <tot_times_to_repeat:
    product=product*number_bad[looper]
    looper=looper+1
msg = "product " + str(product)  
print (product)
