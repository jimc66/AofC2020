# day 4 challenge 2
#
#   7 Fields
#    byr (Birth Year)
#    iyr (Issue Year)
#    eyr (Expiration Year)
#    hgt (Height)
#    hcl (Hair Color)
#    ecl (Eye Color)
#    pid (Passport ID)
#    cid (Country ID)  - THIS ONE IS OPTIONAL / ignored
#
# Each passport is represented as a sequence 
# of key:value pairs separated by spaces or newlines. Passports are separated by blank lines.
#
# Validation: 
#    byr (Birth Year) - four digits; at least 1920 and at most 2002.
#    iyr (Issue Year) - four digits; at least 2010 and at most 2020.
#    eyr (Expiration Year) - four digits; at least 2020 and at most 2030.
#    hgt (Height) - a number followed by either cm or in:
#        If cm, the number must be at least 150 and at most 193.
#        If in, the number must be at least 59 and at most 76.
#    hcl (Hair Color) - a # followed by exactly six characters 0-9 or a-f.
#    ecl (Eye Color) - exactly one of: amb blu brn gry grn hzl oth.
#    pid (Passport ID) - a nine-digit number, including leading zeroes.
#    cid (Country ID) - ignored, missing or not.
#
#
#Your job is to count the passports where all required fields are both present and valid 
#according to the above rules. 

# "Globals"
pp_fields = ['byr', 'iyr', 'eyr', 'hgt', 'hcl', 'ecl', 'pid'] 
#'cid' is optional so we'll totally ignore it
#
# a shot at getting the validation data in one spot - not sure that this really abstracts much
pp_validation = {}
dict_item = {'intmin':1920, 'intmax':2002}
pp_validation['byr'] = dict_item
dict_item = {'intmin':2010, 'intmax':2020}
pp_validation['iyr'] = dict_item
#test=pp_validation['iyr']
dict_item = {'intmin':2020, 'intmax':2030}
pp_validation['eyr'] = dict_item
dict_item = {'cmmin':150, 'cmmax':193, 'cmstr':'cm', 'inmin':59, 'inmax':76, 'instr':'in'}
pp_validation['hgt'] = dict_item
dict_item = {'hairchar':'#', 'validchars':'abcdef0123456789', 'strlen':6}
pp_validation['hcl'] = dict_item
dict_item = {'ecl':True, 'eye':True, 'amb':True, 'blu':True, 'brn':True,
             'gry':True, 'grn':True, 'hzl':True, 'oth':True} 
             # list the valid items that will return true on a lookup?
pp_validation['ecl'] = dict_item
dict_item = {'validchars':'0123456789', 'strlen':9}
pp_validation['pid'] = dict_item

file_name = "day4_input.txt"
key_val_delim = ":"
item_delim = " "

number_bad = 0
number_good = 0
passport_recs = []
passport_rec_num = -1 #starting out with no records


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
    while len(goodstring) > 0:
        goodstring = goodstring.strip() # strip again to handle any leading chars 
        first_separator = goodstring.find(kv_delim)
        if first_separator > 0: # there is an actual item
            key_string = goodstring[0:first_separator]
            end_of_value = goodstring.find(item_delim)
            if end_of_value > first_separator: # we actually found a separator char
                value_string = goodstring[first_separator+1:end_of_value]
                goodstring = goodstring[end_of_value:]
            else: #there was no separator
                value_string = goodstring[first_separator+1:] 
                #the whole rest of the line (which might be nothing)
                goodstring = "" #we just took the rest of the line
            dictionary_items[key_string] = value_string  
    return (dictionary_items)
#############
##  end function parseitems
#############

######
# min max check
# function to check if a value is within range
######
def minmaxcheck(valtocheck, minval, maxval):
    valtocheckint = int(valtocheck)
    if (valtocheckint >= minval) and (valtocheckint <= maxval):
        return True
    else:
        return False


with  open(file_name, 'r') as reader:
    all_lines = reader.read().splitlines()
tot_lines = len(all_lines)-1
reader.close

# loop through the lines
current_line = 0
same_line = False #start with appending a record (the set is blank when we start)
for line in all_lines:
    #get all the multi-line stuff into a set of lines that we actually want to work with
    if len(line) > 0: # this line has data on it
        if same_line:
            passport_recs[passport_rec_num] = passport_recs[passport_rec_num]+line + item_delim #add to the end of the current "record"
        else: #the prior iteration was a blank, add a new record
            passport_recs.append(line + item_delim)
            passport_rec_num = passport_rec_num+1            
        same_line = True # since you just read data, assume you need to stay on the same passport_rec for the next iteration
    else:
        same_line = False
    current_line = current_line+1

#now make our way "down" the file
tot_times_to_repeat = len(passport_recs) # not using this
for current_rec in passport_recs:
    results = parseitems(current_rec, key_val_delim, item_delim)
    good_item = True #approach - check all the fields, if any is missing set it to false
    for afield in pp_fields:
        if not afield in current_rec:
            good_item = False
        else: # it's a matching field, check the validation
            if afield == 'byr': ### ===> STOP RIGHT HERE FOR NOW
                result_check = minmaxcheck(results[afield], pp_validation[afield]['intmin'], 
                               pp_validation[afield]['intmax'])
            elif afield == 'iyr':
                print(results[afield])
                #validation iyr
            elif afield == 'eyr':
                print(results[afield])
                #validation eyr
            elif afield == 'hgt':
                print(results[afield])
                #validation hgt
            elif afield == 'hcl':
                print(results[afield])
                #validation hcl
            elif afield == 'ecl':
                print(results[afield])
                #validation ecl
            elif afield == 'pid':
                print(results[afield])
                #validate pid

    if good_item:
        number_good = number_good+1
    else:
        number_bad = number_bad+1



msg = "good passports " + str(number_good)  
print (msg)
