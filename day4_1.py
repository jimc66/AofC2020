# day 4 challenge 1
#
#   7 Fields
#    byr (Birth Year)
#    iyr (Issue Year)
#    eyr (Expiration Year)
#    hgt (Height)
#    hcl (Hair Color)
#    ecl (Eye Color)
#    pid (Passport ID)
#    cid (Country ID)  - THIS ONE IS OPTIONAL
#
# Each passport is represented as a sequence 
# of key:value pairs separated by spaces or newlines. Passports are separated by blank lines.
#
# Count the number of valid passports - those that have all required fields. 
# Treat cid as optional. In your batch file, how many passports are valid?

# "Globals"
pp_fields =['byr','iyr','eyr','hgt','hcl','ecl','pid'] # 'cid' is optional
file_name="day4_input.txt"
key_val_delim=":"
item_delim=" "

number_bad=0
number_good=0
passport_recs=[]
passport_rec_num=-1 #starting out with no records


#############
# parse items function
# takes a string, and parses the key value pairs into a dict structure
# input: 
# itemstring: a string that contains one or more key:value pairs
# kv_delim: the delimitter between the key and the value
# item_delim: if there are more than 1 items in the string, this is the "separator" between items
#
# return value:
# dictionary of key value pairs
############
def parseitems(itemstring, kv_delim, item_delim):
    # parse the items into a dictionary here
    #
    dictionary_items = {}
    goodstring = itemstring.strip() #clean out any leading or trailing "junk" before we start
    while len (goodstring) > 0:
        goodstring = goodstring.strip() # strip again to handle any leading chars 
        first_separator = goodstring.find(kv_delim)
        if first_separator > 0: # there is an actual item
            key_string = goodstring[0:first_separator]
            end_of_value=goodstring.find(item_delim)
            if end_of_value > first_separator: # we actually found a separator char
                value_string=goodstring[first_separator+1:end_of_value]
                goodstring=goodstring[end_of_value:]
            else: #there was no separator
                value_string=goodstring[first_separator+1:] #the whole rest of the line (which might be nothing)
                goodstring="" #we just took the rest of the line
            dictionary_items[key_string] = value_string  
    return (dictionary_items)
#############
##  end function parseitems
#############

with  open(file_name, 'r') as reader:
    all_lines=reader.read().splitlines()
tot_lines = len(all_lines)-1
reader.close

# loop through the lines
current_line=0
same_line=False #start with appending a record (the set is blank when we start)
for line in all_lines:
    #get all the multi-line stuff into a set of lines that we actually want to work with
    if len(line)>0: # this line has data on it
        if same_line:
            passport_recs[passport_rec_num]=passport_recs[passport_rec_num]+line + item_delim #add to the end of the current "record"
        else: #the prior iteration was a blank, add a new record
            passport_recs.append(line + item_delim)
            passport_rec_num=passport_rec_num+1            
        same_line=True # since you just read data, assume you need to stay on the same passport_rec for the next iteration
    else:
        same_line=False
    current_line=current_line+1

#now make our way "down" the file
tot_times_to_repeat = len(passport_recs) # not using this
for current_rec in passport_recs:
    results= parseitems (current_rec,key_val_delim,item_delim)
    good_item = True #approach - check all the fields, if any is missing set it to false
    for afield in pp_fields:
        if not afield in current_rec:
            good_item = False
    if good_item:
        number_good=number_good+1
    else:
        number_bad=number_bad+1



msg = "good passports " + str(number_good)  
print (msg)
