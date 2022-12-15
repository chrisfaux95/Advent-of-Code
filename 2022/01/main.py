with open('input.txt') as file:
    lines = file.readlines()
inputlist = [x[:-1] for x in lines]


def getelves(inp):
    elves = []
    currentelf = 0
    for i in inp:
        if i != '':
            currentelf += int(i)
        else:
            elves.append(currentelf)
            currentelf = 0
    elves.append(currentelf)
    return (elves)


def part_one():
    elves = getelves(inputlist)
    return (max(elves))


def part_two():
    elves = getelves(inputlist)
    sorted_elves = sorted(elves, reverse=True)
    return sum(sorted_elves[0:3])


print(part_one())
print(part_two())
