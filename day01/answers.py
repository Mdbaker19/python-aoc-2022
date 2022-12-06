from pathlib import Path

prod = Path('./day01/data.txt')
test = Path('./day01/sample.txt')

def sumElfCals(file):
    data = file.read_text()
    data_arr = data.split('\n')
    calorie_sum = 0
    elfs_list = []
    for line in data_arr:
        if line == '':
            elfs_list.append(calorie_sum)
            calorie_sum = 0
        else:
            calorie_sum += int(line)
    return elfs_list


def getKeyFromValueInDict(dict, value):
    for k in dict.keys():
        if dict[k] == value:
            return k


def sumOfMap(dict):
    sum = 0
    for k in list(dict.values()):
        sum += k
    return sum


def day01Pt1Solve(file):
    return max(sumElfCals(file))


# create a dictionary with 3 keys, put those in a list, get the min and compare to the next iteration
# replace the value that is min in the dict, store to list after? and reduce

def day02PtSolve(file):
    elf_calorie_totals = sumElfCals(file)
    cal_map = {0: 0, 1: 0, 2: 0}
    for calorie_total in elf_calorie_totals:
        lowest_total_dict_value = min(list(cal_map.values()))

        '''
        lowest_total_index = list(cal_map.values()).index(lowest_total_dict_value)
        # get the key that holds this current min,
        # create a list of the keys and index it with index of lowest in a list of values from dict
        key = list(cal_map.keys())[lowest_total_index]
        '''

        key = getKeyFromValueInDict(cal_map, lowest_total_dict_value)

        if calorie_total > lowest_total_dict_value:
            cal_map[key] = calorie_total

    return sumOfMap(cal_map)


# print(day01Pt1Solve(test))
# print(day01Pt1Solve(prod))

# print(day02PtSolve(test))
# print(day02PtSolve(prod))
