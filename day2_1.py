# How many passwords are valid according to their policies?
number_good=0
number_bad=0
file_name="day2_input.txt"

with open(file_name, 'r') as reader:
    for line in reader:
#        print (line)
        line=line.rstrip() # clean up the end of line
        min_instance_endloc=line.find("-")
        min_instance_str=line[0:min_instance_endloc]
        min_instance_int=int(min_instance_str)
        max_instance_endloc=line.find(" ")
        max_instance_str=line[min_instance_endloc+1:max_instance_endloc]
        max_instance_int=int(max_instance_str)
        char_instance_endloc=line.find(":")
        char_instance_str=line[max_instance_endloc+1:char_instance_endloc]
        pw_startloc=line.find(": ")
        pw_string=line[pw_startloc+2:]
        number_instances=pw_string.count(char_instance_str)
        if (number_instances >= min_instance_int) and (number_instances <= max_instance_int):
            number_good = number_good + 1
        else:
            number_bad = number_bad + 1

#        min_instance_int=int(min_instance_str)
msg = "good pw: " + str(number_good) + "   bad pw: " + str(number_bad) 
print (msg)
reader.close