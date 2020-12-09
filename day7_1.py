"""
advent of code day 1 challenge number 1

Due to recent aviation regulations, many rules
(your puzzle input) are being enforced about bags
and their contents; bags must be color-coded and must
contain specific quantities of other color-coded bags.

How many bag colors can eventually contain
at least one shiny gold bag? (The list of rules is quite long;
make sure you get all of it.)


"""

# "Globals"
FILE_NAME = "day7_input.txt"
#FILE_NAME = "testinput_7.txt"

def removebag (bagstr):
    """
    removebag

    takes a string (bagstr)
    removes the trailing 
    ' bag' or ' bags'
    returns a string
    """
    if bagstr[-4:] == ' bag':
        return bagstr[0:-4]
    if bagstr[-5:] == ' bags':
        return bagstr[0:-5]
    return bagstr #found no match

def findbag (bagdict, bagstr):
    """
    findbag

    takes a nested dictionary (bagdict)
    finds all the instances of the bag (bagstr)
    returns a list of the bags that contain this bag (return_list)
    """
    return_list = []
    top_level_key = ''
    for key, value in bagdict.items():
        top_level_key = key
        if key == bagstr:
            return_list.append(key)
        elif isinstance(value, dict): #recursively call findbag
            results = findbag (value,bagstr)
            for result in results:
                return_list.append(top_level_key) #return top key for embedded bag
            #    return_list.append(result) 
    return return_list #found no match

def parsebags(listofbags):
    """
    parsebags
    takes as input a list of strings (listofbags)
    returns a list of nested dictionary items (final_dict)
    that contains all the bag 'recipes'
    """
    final_dict = {}
    bag_contents = {}
    checkloop=0
    listlen = len(listofbags)
    for line in listofbags:
        #get all the multi-line stuff into a set of lines that we actually want to work with
        if len(line)>0: # this line has data on it
            splitter = line.split('contain')
            top_level_bag = splitter[0].strip()
            top_level_bag = removebag(top_level_bag)
            bag_contents[top_level_bag] = {}
            rightsplit = splitter[1].split(',')
            for items in rightsplit:
                raw_bag = items.strip() #get rid of whitespace
                if raw_bag[-1] == '.': #the last one has a .
                    raw_bag = raw_bag[:-1]
                if not raw_bag == 'no other bags':
                    one_bag_list = raw_bag.split(' ',1) #take the first number, leave the rest
                    num_items_in_bag = int (one_bag_list[0]) 
                    bag_in_bag = one_bag_list[1].strip() #clean up leading or trailing spaces
                    bag_in_bag = removebag(bag_in_bag) # get rid of trailing bag string
                    bag_contents[top_level_bag][bag_in_bag] = num_items_in_bag
                else:
                    bag_contents[top_level_bag]['empty'] = True #empty means nothing in it
    return bag_contents


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
    all_bag_entries = {} #for the dictionary of all bags
    gold_ones = {}
    all_bag_entries = parsebags(all_lines)
    gold_ones = findbag(all_bag_entries, 'shiny gold')
    new_bags = []
    for bag in gold_ones:
        new_ones = findbag(all_bag_entries, bag)
        for items in new_ones:
            if not items in gold_ones:
                gold_ones.append(items)
    total_bags = len(gold_ones) -1 #subtract gold
    msg = 'total bags: ' + str(total_bags)
    print(msg)
#    total = sumentries(all_group_entries)
#    msg = "grand total: " + str(total)
#    print(msg)

#call the main function
main()
