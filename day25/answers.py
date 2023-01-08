from pathlib import Path
from math import pow

def createDataArr(file):
    data = file.read_text()
    return data.split('\n')


prod = createDataArr(Path('./day25/data.txt'))
test = createDataArr(Path('./day25/sample.txt'))

dict = {'=': -2, '-': -1}


# evaluate each value based on position in the snafu number, push that into an array?
# ex: [625, -250, -25, 0, 1] => 976
def day25Pt1Solve(data):
    total = 0
    print("Data: ", data)
    for snafu in data:
        value = getValue(snafu)
        print("Value: ", value)
        for v in value:
            total += v
    return convertToSnafu(total)


# determine the largest 5 to the power of 'x' that is less than total passed in
# that will be the initial len of the output Snafu...?
#  no idea..
def convertToSnafu(total):

    return total


def getValue(snafu):
    print("Snafu working with: ", snafu)
    str_len = len(snafu) - 1
    snafu_list = []
    for idx, digit in enumerate(str(snafu)):
        # str_len - idx is the 5 to x power
        val = round(pow(5, str_len - idx))
        digit_val = digit
        if digit in dict:
            digit_val = dict[digit]
        snafu_list.append(val * int(digit_val))
    return snafu_list


# print(getValue('2=-1=0'))  # 976
print(day25Pt1Solve(['2=-1=0']))
# print(convertToSnafu(4890))  # '2=-1=0

# print(day25Pt1Solve(test))
print(day25Pt1Solve(prod))


# print(day25Pt2Solve(test))
# print(day25Pt2Solve(prod))

