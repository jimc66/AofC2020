# Starting at the top-left corner of your map and following a slope of right 3 and down 1,
# how many trees would you encounter?
number_good=0
number_bad=0
file_name="day3_input.txt"
curr_pos=[0,0]
x_move=3
y_move=1
tree_char="#"
clear_char="."

with  open(file_name, 'r') as reader:
    all_lines=reader.read().splitlines()
tot_lines = len(all_lines)-1

# figure out how "wide" the strings need to be
line_length=len(all_lines[0])
length_needed=tot_lines * x_move
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
y_pos=0
x_pos=0
while y_pos <tot_lines:
    y_pos=y_pos+y_move
    x_pos=x_pos+x_move
    pos_char= all_lines[y_pos][x_pos]
    if pos_char == tree_char:
        number_bad=number_bad+1
    else:
        number_good=number_good+1

msg = "good spots: " + str(number_good) + "   bad spots: " + str(number_bad) 
print (msg)
reader.close