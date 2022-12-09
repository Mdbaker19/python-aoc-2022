from pathlib import Path
from util import createDataArr

prod = createDataArr(Path('./day03/data.txt'))
test = createDataArr(Path('./day03/sample.txt'))

# each line, split in half and compare, find the match and get that 'score'
# from a dict, built out by separate fn

lower_str = 'abcdefghijklmnopqrstuvwxyz'
upper_str = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'


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
print(day03Pt1Solve(prod))
