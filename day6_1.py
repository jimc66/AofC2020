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
def parselines(the_lines):
    """
    getentries

    read in all the lines
    figure out the delimitter between groups
    add each unique item per group to a dictionary
    add the dictionary entries to a list
    return that list of dictionary items that have the unique entries
    """
    dict_item = {}
    list_of_dict_items = []
    for line in the_lines:
        #get all the multi-line stuff into a set of lines that we actually want to work with
        if len(line)>0: # this line has data on it
            for character in line:
                dict_item[character] = True #add them in, don't care if it's overwritting
        else: # when you get a blank line, add a new record and clear dict_item
            list_of_dict_items.append(dict_item.copy()) # need a copy, not a reference
            dict_item.clear()
    list_of_dict_items.append(dict_item.copy()) # add the last item
    return list_of_dict_items

def sumentries(listofdictionaries):
    """
    sumentries

    add total number of entries (using length)
    """
    grand_total = 0
    for dictitem in listofdictionaries:
        grand_total = grand_total + len(dictitem)
    return grand_total

def main():
    """
    main module
    """
    with  open(FILE_NAME, 'r') as reader:
        all_lines = reader.read().splitlines()
    reader.close
    all_group_entries = [] #for the list of all the groups
    all_group_entries = parselines(all_lines)
    total = sumentries(all_group_entries)
    msg = "grand total: " + str(total)
    print(msg)

#call the main function
main()
