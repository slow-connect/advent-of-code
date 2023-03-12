input = open('Day03-imput.txt', 'r')

def p1(input):
    lines = input.readlines()
    for k in range(len(lines)):
        lines[k] = list(lines[k].replace('\n', ''))
    gamma = []
    for l in range(len(lines[0])):
        zero, one = 0, 0
        for k in range(len(lines)):
            if lines[k][l] == '0':
                zero += 1
            else:
                one += 1
        if zero > one:
            gamma.append('0')
        else:
            gamma.append('1')
    epsilon = []
    for k in range(len(gamma)):
        if gamma[k] == '0':
            epsilon.append('1')
        else:
            epsilon.append('0')
    str1 = ''
    str2 = ''
    for k in range(len(gamma)):
        str1 += gamma[k]
        str2 += epsilon[k]
    print(int(str1, 2) * int(str2, 2))


def p2(input):
    lines = input.readlines()
    # print(lines)
    for k in range(len(lines)):
        lines[k] = list(lines[k].replace('\n', ''))
    lines.sort()
    co2lines = lines.copy()
    o2lines = lines.copy()
    co2value = []
    o2value = []
    for l in range(12):
        one, zero = 0, 0
        for k in range(len(o2lines)):
            if o2lines[k][l] == '0':
                zero += 1
            else:
                one += 1
        if one >= zero:
            val = '1'
            o2value.append('1')
        else:
            val = '0'
            o2value.append('0')
        newo2 = []
        for k in range(len(o2lines)):
            if o2lines[k][l] == val:
                newo2.append(o2lines[k])
            else:
                pass
        o2lines = newo2
        if len(o2lines) == 1:
            o2value = o2lines[0]
            break
    for l in range(12):
        one, zero = 0, 0
        for k in range(len(co2lines)):
            if co2lines[k][l] == '0':
                zero += 1
            else:
                one += 1
        if zero <= one:
            val = '0'
            o2value.append('0')
        else:
            o2value.append('1')
            val = '1'
        newco2 = []
        for k in range(len(co2lines)):
            if co2lines[k][l] == val:
                newco2.append(co2lines[k])
            else:
                pass
        co2lines = newco2
        if len(co2lines) == 1:
            co2value = co2lines[0]
            break
    ## Why o2value gets longer then 12 bits is still a mystery to me, but this gives the right result...
    print(int(''.join(co2value), 2) * int(''.join(o2value[0:12]), 2))




p2(input)
