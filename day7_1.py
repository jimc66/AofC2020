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

def removebag(bagstr):
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

def findbag(bagdict, bagstr):
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
            results = findbag(value, bagstr)
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
    bag_contents = {}
    for line in listofbags:
        #get all the multi-line stuff into a set of lines that we actually want to work with
        if len(line) > 0: # this line has data on it
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
                    one_bag_list = raw_bag.split(' ', 1) #take the first number, leave the rest
                    num_items_in_bag = int(one_bag_list[0])
                    bag_in_bag = one_bag_list[1].strip() #clean up leading or trailing spaces
                    bag_in_bag = removebag(bag_in_bag) # get rid of trailing bag string
                    bag_contents[top_level_bag][bag_in_bag] = num_items_in_bag
                else:
                    bag_contents[top_level_bag]['empty'] = True #empty means nothing in it
    return bag_contents

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
    for bag in gold_ones:
        new_ones = findbag(all_bag_entries, bag)
        for items in new_ones:
            if not items in gold_ones:
                gold_ones.append(items)
    total_bags = len(gold_ones) -1 #subtract gold
    msg = 'total bags: ' + str(total_bags)
    print(msg)

#call the main function
main()
