def day02Pt1Solve(file):
    data = file.read_text()
    data_arr = data.split('\n')

    score = 0

    for pair in data_arr:
        plays_dict[pair][0] += 1

    for play in plays_dict:
        if plays_dict[play][0] == 0:
            pass
        else:
            instances = plays_dict[play][0]
            for i in range(instances):
                your_play = play.split(' ')[0]
                score += plays_dict[play][1]
                score += score_dict[your_play]

    return score