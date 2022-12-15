with open('input.txt') as file:
    lines = file.readlines()
inputlist = [x[:-1] for x in lines]


def lettervalue(c):
    ch = ''.join(c)
    if not ch.isupper():
        return ord(ch) - 96
    else:
        return ord(ch) - 38


def part_one():
    bagslist = [(x[0:int(len(x)/2)], x[int(len(x)/2):]) for x in lines]
    duplicates = [list(set(x[0]) & set(x[1]))[0] for x in bagslist]
    duplicatesum = sum([lettervalue(x) for x in duplicates])
    print(duplicatesum)


def part_two():
    groupslist = []
    for i in range(0, len(inputlist), 3):
        groupslist.append([inputlist[i], inputlist[i+1], inputlist[i+2]])
    badgelist = [list(set(x[0]) & set(x[1]) & set(x[2])) for x in groupslist]
    badgesum = sum([lettervalue(x) for x in badgelist])
    print(badgesum)


part_one()
part_two()
