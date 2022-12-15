from itertools import filterfalse
with open('input.txt') as file:
    # with open('test.txt') as file:
    cratesinput, instructionslist = file.read().split('\n\n')


# CRATES SETUP
cratesinput = cratesinput.split('\n')
cratesinput = list(zip(*reversed(cratesinput)))
cratesinput = [list(x) for x in cratesinput]
def nospace(i): return i[0] == ' '


cratesinput = list(filterfalse(nospace, cratesinput))
cratesinput = [list(filterfalse(nospace, x)) for x in cratesinput]
cratesinput = [x[1:] for x in cratesinput]


# INSTRUCTIONS SETUP
instructionslist = instructionslist.split('\n')
instructionslist = instructionslist[:-1]
instructionslist = [x.split() for x in instructionslist]
instructionslist = [[x[1], x[3], x[5]] for x in instructionslist]
instructionslist = [[int(y) for y in x] for x in instructionslist]


def part_one():
    crates = cratesinput[::]
    for i in instructionslist:
        count, position, dest = i
        position = int(position) - 1
        dest = int(dest) - 1
        for i in range(count):
            crates[dest].append(crates[position].pop())
    solution = ''.join([x[-1] for x in crates])
    print(crates)
    print('Part One: ', solution)


part_one()
