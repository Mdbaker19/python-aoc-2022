from pathlib import Path

prod = Path('./day02/data.txt')
test = Path('./day02/sample.txt')


score_dict = {
    'X': 1, 'Y': 2, 'Z': 3
}

score_dict_op = {
    'A': 1, 'B': 2, 'C': 3
}

# score given based off your_play in part 2
score_dict_2 = {
    'X': 0, 'Y': 3, 'Z': 6
}

# contains each play [0] - occurrence, [0] score for that occurrence
plays_dict = {
    'A X': [0, 3], 'A Y': [0, 6], 'A Z': [0, 0],
    'B X': [0, 0], 'B Y': [0, 3], 'B Z': [0, 6],
    'C X': [0, 6], 'C Y': [0, 0], 'C Z': [0, 3]
}

# determine points for what I play
# determine if it is a win, lose or draw
# store each pair into a dict with a count of each occurrence - [a x, a y, a z, b x, ...]


def day02Pt2Solve(file):
    data = file.read_text()
    data_arr = data.split('\n')

    score = 0

    for pair in data_arr:
        plays_dict[pair][0] += 1

    for play in plays_dict:
        # based off the play.split(' ')[1] => that is outcome score
        # determine what needs to be played based off opponent play
        #   op play is play.split(' ')[0]
        #   map op play to corresponding your play based off desired result

        op_play, your_play = play.split(' ')
        pass

    return score


# print(day02Pt1Solve(test))
# print(day02Pt1Solve(prod))

print(day02Pt2Solve(test))
# print(day02Pt2Solve(prod))
