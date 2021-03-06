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
PP_FIELDS = ['byr', 'iyr', 'eyr', 'hgt', 'hcl', 'ecl', 'pid']
#'cid' is optional so we'll totally ignore it
#
# a shot at getting the validation data in one spot - not sure that this really abstracts much
PP_VALIDATION = {}
DICT_ITEM = {'intmin':1920, 'intmax':2002}
PP_VALIDATION['byr'] = DICT_ITEM
DICT_ITEM = {'intmin':2010, 'intmax':2020}
PP_VALIDATION['iyr'] = DICT_ITEM
#test=PP_VALIDATION['iyr']
DICT_ITEM = {'intmin':2020, 'intmax':2030}
PP_VALIDATION['eyr'] = DICT_ITEM
DICT_ITEM = {'cmmin':150, 'cmmax':193, 'cmstr':'cm', 'inmin':59, 'inmax':76, 'instr':'in'}
PP_VALIDATION['hgt'] = DICT_ITEM
DICT_ITEM = {'hairchar':'#', 'validchars':'abcdef0123456789', 'strlen':6}
PP_VALIDATION['hcl'] = DICT_ITEM
DICT_ITEM = {'ecl':True, 'eye':True, 'amb':True, 'blu':True, 'brn':True,
             'gry':True, 'grn':True, 'hzl':True, 'oth':True}
             # list the valid items that will return true on a lookup?
PP_VALIDATION['ecl'] = DICT_ITEM
DICT_ITEM = {'validchars':'0123456789', 'strlen':9}
PP_VALIDATION['pid'] = DICT_ITEM

FILE_NAME = "day4_input.txt"
KEY_VAL_DELIM = ":"
ITEM_DELIM = " "



#############
# parse items function
# takes a string, and parses the key value pairs into a dict structure
# input:
# itemstring: a string that contains one or more key:value pairs
# kv_delim: the delimitter between the key and the value
# ITEM_DELIM: if there are more than 1 items in the string, this is the "separator" between items
#
# return value:
# dictionary of key value pairs
############
def parseitems(itemstring, kv_delim, item_delimiter):
    # parse the items into a dictionary here
    #
    dictionary_items = {}
    goodstring = itemstring.strip() #clean out any leading or trailing "junk" before we start
    while len(goodstring) > 0:
        goodstring = goodstring.strip() # strip again to handle any leading chars
        first_separator = goodstring.find(kv_delim)
        if first_separator > 0: # there is an actual item
            key_string = goodstring[0:first_separator]
            end_of_value = goodstring.find(item_delimiter)
            if end_of_value > first_separator: # we actually found a separator char
                value_string = goodstring[first_separator+1:end_of_value]
                goodstring = goodstring[end_of_value:]
            else: #there was no separator
                value_string = goodstring[first_separator+1:]
                #the whole rest of the line (which might be nothing)
                goodstring = "" #we just took the rest of the line
            dictionary_items[key_string] = value_string
    return dictionary_items
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

######
# height check
# function to check if a value is within range
# pass in the string to check, the dictionary of the check values, the key to get there (i.e. hgt)
######
def heightcheck(valtocheck, dictkey):
    cm_loc = valtocheck.find(PP_VALIDATION[dictkey]['cmstr'])
    if cm_loc < 0: # try inches if no cm
        inch_loc = valtocheck.find(PP_VALIDATION[dictkey]['instr'])
        valtocheckstr = valtocheck[0:inch_loc]
        valtocheckint = int(valtocheckstr)
        minval = PP_VALIDATION[dictkey]['inmin']
        maxval = PP_VALIDATION[dictkey]['inmax']
    else: #it IS cm
        valtocheckstr = valtocheck[0:cm_loc]
        valtocheckint = int(valtocheckstr)
        minval = PP_VALIDATION[dictkey]['cmmin']
        maxval = PP_VALIDATION[dictkey]['cmmax']
#    PP_VALIDATION[afield]['intmax']
#    valtocheck_numberpart=
#    valtocheckint = int(valtocheck)
#    cmmin':150, 'cmmax':193, 'cmstr':'cm', 'inmin':59, 'inmax':76, 'instr':'in'
    if (valtocheckint >= minval) and (valtocheckint <= maxval):
        return True
    else:
        return False

######
# hair check
# function to check if a value is within range
# pass in the string to check, the dictionary of the check values, the key to get there (i.e. hcl)
######
def haircheck(valtocheck, dictkey):
    if len(valtocheck) > 0: #mildly defensive...
        first_char = valtocheck[0]
        val_without_zero = valtocheck[1:]
    val_length = len(val_without_zero)
    allowed_set = set(PP_VALIDATION[dictkey]['validchars'])
    if (first_char == PP_VALIDATION[dictkey]['hairchar']) and (val_length == PP_VALIDATION[dictkey]['strlen']) and (set(val_without_zero).issubset(allowed_set)):
        return True
    else:
        return False


######
# eye check
# function to check if a value is within range
# pass in the string to check, the dictionary of the check values, the key to get there (i.e. ecl)
######
def eyecheck(valtocheck, dictkey):
    if valtocheck in PP_VALIDATION[dictkey]: #mildly defensive...
        # since they are set to true.
        return PP_VALIDATION[dictkey][valtocheck]
    else:
        return False

######
# passport check
# function to check if a value is within range
# pass in the string to check, the dictionary of the check values, the key to get there (i.e. pid)
######
def passportcheck(valtocheck, dictkey):
    if len(valtocheck) > 0: #mildly defensive...
        val_length = len(valtocheck)
        allowed_set = set(PP_VALIDATION[dictkey]['validchars'])
        if val_length == PP_VALIDATION[dictkey]['strlen'] and set(valtocheck).issubset(allowed_set):
            return True
        else:
            return False
    else:
        return False


##################################
#
#  main
#
###################################
def main():
    number_bad = 0
    number_good = 0
    passport_recs = []
    passport_rec_num = -1 #starting out with no records
    with  open(FILE_NAME, 'r') as reader:
        all_lines = reader.read().splitlines()
#    tot_lines = len(all_lines)-1
    reader.close

    # loop through the lines
    current_line = 0
    same_line = False #start with appending a record (the set is blank when we start)
    for line in all_lines:
        #get all the multi-line stuff into a set of lines that we actually want to work with
        if len(line) > 0: # this line has data on it
            if same_line:
                passport_recs[passport_rec_num] = passport_recs[passport_rec_num]+line + ITEM_DELIM
                            #add to the end of the current "record"
            else: #the prior iteration was a blank, add a new record
                passport_recs.append(line + ITEM_DELIM)
                passport_rec_num = passport_rec_num+1
            same_line = True # since you just read data, assume you need to stay on the same
                            #passport_rec for the next iteration
        else:
            same_line = False
        current_line = current_line+1

    #now make our way "down" the file
 #   tot_times_to_repeat = len(passport_recs) # not using this
    for current_rec in passport_recs:
        results = parseitems(current_rec, KEY_VAL_DELIM, ITEM_DELIM)
        good_item = True #approach - check all the fields, if any is missing set it to false
        for afield in PP_FIELDS:
            if not afield in current_rec:
                good_item = False
            else: # it's a matching field, check the validation
                this_good_item = False #start  with assuming a problem?
                # if any of the validation fails, set good_item to false
                # if it makes it all the way through then it stays "good"
                if afield == 'byr':
                    this_good_item = minmaxcheck(results[afield], PP_VALIDATION[afield]['intmin'],
                                                 PP_VALIDATION[afield]['intmax'])
                elif afield == 'iyr':
                    this_good_item = minmaxcheck(results[afield], PP_VALIDATION[afield]['intmin'],
                                                 PP_VALIDATION[afield]['intmax'])
                elif afield == 'eyr':
                    this_good_item = minmaxcheck(results[afield], PP_VALIDATION[afield]['intmin'],
                                                 PP_VALIDATION[afield]['intmax'])
                elif afield == 'hgt':
                    this_good_item = heightcheck(results[afield], afield)
                    #validation hgt
                elif afield == 'hcl':
                    this_good_item = haircheck(results[afield], afield)
                    #validation hcl
                elif afield == 'ecl':
                    this_good_item = eyecheck(results[afield], afield)
                elif afield == 'pid':
                    this_good_item = passportcheck(results[afield], afield)
            # if we got a validation failure, set item bad and break out of
            # the for afield loop
            if this_good_item == False:
                good_item = False
                break


        if good_item:
            number_good = number_good+1
        else:
            number_bad = number_bad+1



    msg = "good passports " + str(number_good)
    print(msg)

#call the main function
main()
