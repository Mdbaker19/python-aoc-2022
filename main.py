from pathlib import Path


def createDataArr(file):
    data = file.read_text()
    return data.split('\n')


prod = createDataArr(Path('./day06/data.txt'))
test = createDataArr(Path('./day06/sample.txt'))


def day06Solve(data, is_test=False, is_pt2=False):
    copy_len = 4
    if is_pt2:
        copy_len = 14
    if is_test:
        idxs = []
        for d in data:
            for c in range(len(d) - copy_len):
                sub_str = d[c:c+copy_len]
                contains_copy = isThereCopy(sub_str)
                if not contains_copy:
                    idxs.append(c + copy_len)
                    break
        return idxs
    else:
        d = data[0]
        for c in range(len(d) - copy_len):
            sub_str = d[c:c + copy_len]
            contains_copy = isThereCopy(sub_str)
            if not contains_copy:
                return c + copy_len
    return ''


# create dict and check that unique keys in dict is of len 4?
def isThereCopy(sub_str):
    letter_count = {}
    for c in sub_str:
        if c in letter_count:
            return True
        else:
            letter_count[c] = 1
    return False


print(day06Solve(test, True))
print(day06Solve(test, True, True))
print(day06Solve(prod, False, True))
