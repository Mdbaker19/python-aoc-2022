from pathlib import Path


def createDataArr(file):
    data = file.read_text()
    return data.split('\n')


def parseData(data):
    for idx, line in enumerate(data):
        if len(line.split(' ')) > 1:
            return data[:idx], data[idx:]
    return '', ''


prod = createDataArr(Path('./day05/data.txt'))
test = createDataArr(Path('./day05/sample.txt'))

# create strings of each char stack set and pull substring sections off each
# based off what needs to be moved where
# ['D', 'NC', 'ZMP']
# move 1 from 2 to 1
# array[2][:1] # get one off end
# concat that to 1
# try this
def day05Pt1Solve(data, part_01=True):
    # need to parse out the values in each stack
    # ignore the 1 2 3
    # remove the [] from each and white space
    parsed_data, steps = parseData(data)
    print(parsed_data)
    print(steps)

    for step in steps:
        step_arr = step.split(' ')
        amount = int(step_arr[1])
        from_stack = int(step_arr[3]) - 1
        to_stack = int(step_arr[5]) - 1

        take_chars = parsed_data[from_stack][:amount]
        replace_chars = parsed_data[from_stack][amount:]

        parsed_data[from_stack] = replace_chars
        # print('take chars: ', take_chars, ' added to ', parsed_data[to_stack])
        # the take chars need to be looped over and added to the parsed_data[to_stack]

        if part_01:
            build_str_stack = ''
            for c in reversed(take_chars):
                build_str_stack += c
            parsed_data[to_stack] = build_str_stack + str(parsed_data[to_stack])
        else:
            parsed_data[to_stack] = take_chars + str(parsed_data[to_stack])


        print(parsed_data)


    output = ''

    for s in parsed_data:
        if len(s) >= 1:
            output += s[:1]

    return output


# print(day05Pt1Solve(test, False))
print(day05Pt1Solve(prod, False))


# print(day05Pt2Solve(test))
# print(day05Pt2Solve(prod))
