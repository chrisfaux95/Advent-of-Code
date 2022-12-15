with open('input.txt') as file:
    lines = file.readlines()
inputlist = lines


def lettervalue(ch):
    if not ch.isupper():
        return ord(ch) - 96
    else:
        return ord(ch) - 38


def part_one():
    bagslist = [(x[0:int(len(x)/2)], x[int(len(x)/2):]) for x in lines]
    duplicates = [list(set(x[0]) & set(x[1]))[0] for x in bagslist]
    duplicatesum = sum([lettervalue(x) for x in duplicates])
    print(duplicatesum)


part_one()
