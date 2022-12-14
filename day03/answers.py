from pathlib import Path
from util import createDataArr

prod = createDataArr(Path('./day03/data.txt'))
test = createDataArr(Path('./day03/sample.txt'))

# each line, split in half and compare, find the match and get that 'score'
# from a dict, built out by separate fn

lower_str = 'abcdefghijklmnopqrstuvwxyz'
upper_str = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'

# Absolute python mess right now but went a way with it and now trying to figure that way out..
# good luck when you're back


def buildLowerMap():
    dict = {}
    for i, c in enumerate(lower_str):
        dict[c] = i + 1
    return dict


def buildUpperMap():
    dict = {}
    for i, c in enumerate(upper_str):
        dict[c] = i + 1 + 26
    return dict


lower_score_map = buildLowerMap()
upper_score_map = buildUpperMap()


def getMatchChar(first_half, second_half):
    match = ''
    for a, c in zip(first_half, second_half):
        if second_half.find(a) >= 0:
            match = a
        elif first_half.find(c) >= 0:
            match = c

    return match


def day03Pt1Solve(data):
    score = 0
    for line in data:
        first_half = line[0:round(len(line) / 2)]
        second_half = line[round(len(line) / 2):]
        match_char = getMatchChar(first_half, second_half)
        if match_char.isupper():
            score += upper_score_map[match_char]
        elif match_char.islower():
            score += lower_score_map[match_char]
    return score


# print(day03Pt1Solve(test))
# print(day03Pt1Solve(prod))

# return the set of words as dictionaries from countCharsDict() and
# pass through those with a but with the longest string based of variety of chars
# so pass through coutCharsDict, get len of key() from each and
# pass through longest by
def getLongest(rucksacks):
    # d1, d2, d3 = group_set.stream().map(group -> countCharsDict(group)).make into a tuple (x, x, x);
    dict_list = []
    for i in range(len(rucksacks)):
        dict_list.append(countCharsDict(rucksacks[i]))

    # print("letterCounts: ", dict_list)

    # get the longest list by keys
    print(dict_list)
    key_len_list = []
    bound_dicts = {}
    for d in dict_list:
        l = len(d.keys())
        bind_dict = {l: d}
        key_len_list.append(l)
        bound_dicts[l] = bind_dict


    # bind the array of strings to their lens to then be referenced later


    # get the longest len dictionary of unique characters to use as the one to loop
    # over to check for the common char
    most_unique_chars = bound_dicts[key_len_list[len(key_len_list) - 1]][key_len_list[len(key_len_list) - 1]]

    for char in most_unique_chars:
        pass

    return most_unique_chars


# this does mutate the list passed in
def sortNumList(list):
    for i, num in enumerate(list):
        inner_idx = i
        while inner_idx > 0 and num < list[inner_idx - 1]:
            # swap list[i] with list[i + 1]
            a = list[inner_idx]
            list[inner_idx] = list[inner_idx - 1]
            list[inner_idx - 1] = a
            inner_idx -= 1

            # print(a, list[i], list[i + 1], inner_idx, i)
    return list


def countCharsDict(string):
    dict = {}
    for c in string:
        if c in dict:
            dict[c] = dict[c] + 1
        else:
            dict[c] = 1

    return dict


# print(countCharsDict('hello There today is good'))


# split data into groups of 3, find the match of each set of 3 and calc points
def day03Pt2Solve(data):
    # create a list of lists of groups
    group_list = []
    group = []
    counter = 0
    for i, line in enumerate(data):
        group.append(line)
        counter += 1
        if counter % 3 == 0:
            group_list.append(group)
            group = []
            counter = 0

    print('list', group_list)

    # get the longest substring and loop over it to determine char find match

    # get the longest unique chars dictionary from the list of rucksack strings
    # intention was to loop over the keys of the most unique, do a get attempt on
    # the other dictionaries of unique chars (need to get / return those still)
    # if get success, that is the unique to get score from
    score = 0
    for group_set in group_list:
        match_char = ''
        most_unique_chars_dict = getLongest(group_set)
        print(most_unique_chars_dict)

    return score


print(day03Pt2Solve(test))
# print(day03Pt2Solve(prod))
