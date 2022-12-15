with open('input.txt') as file:
    lines = file.readlines()
inputlist = [x[:-1] for x in lines]
# print(l)


def part_one(inp):
    elves = []
    currentelf = 0
    for i in inp:
        if i != '':
            currentelf += int(i)
        else:
            elves.append(currentelf)
            currentelf = 0
    elves.append(currentelf)
    return (max(elves))


def part_two(inp):
    elves = []
    currentelf = 0
    for i in inp:
        if i != '':
            currentelf += int(i)
        else:
            elves.append(currentelf)
            currentelf = 0
    elves.append(currentelf)
    sorted_elves = sorted(elves, reverse=True)
    return sum(sorted_elves[0:3])


print(part_one(inputlist))
print(part_two(inputlist))
