# How many passwords are valid according to their policies?
#Exactly one of these positions must contain the given letter. 
#Other occurrences of the letter are irrelevant for the purposes of policy enforcement.
number_good=0
number_bad=0
file_name="day2_input.txt"

with open(file_name, 'r') as reader:
    for line in reader:
#        print (line)
        line=line.rstrip() # clean up the end of line
        min_instance_endloc=line.find("-")
        min_instance_str=line[0:min_instance_endloc]
        min_instance_int=int(min_instance_str) #keep using min instance - means first position
        max_instance_endloc=line.find(" ")
        max_instance_str=line[min_instance_endloc+1:max_instance_endloc]
        max_instance_int=int(max_instance_str) # keep using max instance- means 2nd position
        char_instance_endloc=line.find(":")
        char_instance_str=line[max_instance_endloc+1:char_instance_endloc]
        pw_startloc=line.find(": ")
        pw_string=line[pw_startloc+2:]
        # check for a match at the first position
        if pw_string[min_instance_int-1] == char_instance_str:
            match_pos1=1
        else:
            match_pos1=0
        # check for a match at the 2nd position
        if pw_string[max_instance_int-1] == char_instance_str:
            match_pos2=1
        else:
            match_pos2=0
        # now, we need to have exactly 1 occurrence of a match
        if (match_pos1 + match_pos2) == 1: 
            number_good = number_good + 1
        else:
            number_bad = number_bad + 1

#        min_instance_int=int(min_instance_str)
msg = "good pw: " + str(number_good) + "   bad pw: " + str(number_bad) 
print (msg)
reader.close