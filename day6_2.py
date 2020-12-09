"""
advent of code day 6 challenge number 2

The form asks a series of 26 yes-or-no questions marked a through z.
All you need to do is identify the questions for which anyone in your
group answers "yes".



For each group, count the number of questions
to which anyone answered "yes". What is the sum of those counts?

"""

# "Globals"
FILE_NAME = "day6_input.txt"
#FILE_NAME = "testinput_6.txt"

def sameitems(dictlist):
    """
    sameitems
    takes as input a list of dictionary items (dictlist)
    returns a single dictionary item (final_dict)
    that contains only the the items that are on every 
    list
    """
    checkloop=1
    dictlistlen = len(dictlist)
    final_dict = dictlist[0] #initial list is the "whole thing"
#   final_final_dict = {}
    while checkloop < dictlistlen:
        final_final_set = final_dict.items() & dictlist[checkloop].items()
        checkloop = checkloop + 1
        # out dictionary is now a set - convert it back so we can do
        # the next comparison
        final_dict.clear() #clear and repopulate final_dict
        for value in final_final_set: 
            final_dict[value[0]] =value[1]
    return final_dict


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
    group_id = 0
    group_list = []
    for line in the_lines:
        #get all the multi-line stuff into a set of lines that we actually want to work with
        if len(line)>0: # this line has data on it
            for character in line:
                dict_item[character] = True #add them in for this person
            group_id = group_id + 1
            group_list.append(dict_item.copy())
            dict_item.clear()
        else: # when you get a blank line, add a new record and clear dict_item
            newdictitem = {}
            newdictitem = sameitems(group_list)
            list_of_dict_items.append(newdictitem.copy()) # need a copy, not a reference
            group_list.clear()
    newdictitem = {}
    newdictitem = sameitems(group_list)
    list_of_dict_items.append(newdictitem.copy()) # add the last item
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
