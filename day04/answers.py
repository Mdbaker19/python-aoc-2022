from pathlib import Path
from util import createDataArr

prod = createDataArr(Path('./day04/data.txt'))
test = createDataArr(Path('./day04/sample.txt'))


def day04Pt1Solve(data):


    single_job_count = 0

    for pair in data:
        first, second = pair.split(',')
        first_low, first_high = first.split('-')
        second_low, second_high = second.split('-')

        if first_low <= second_low and first_high >= second_high:
            single_job_count += 1
        elif first_low >= second_low and first_high <= second_high:
            single_job_count += 1


    return single_job_count



print(day04Pt1Solve(test))
print(day04Pt1Solve(prod))


# print(day04Pt2Solve(test))
# print(day04Pt2Solve(prod))
