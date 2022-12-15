with open('input.txt') as file:
    lines = file.readlines()
inputlist = [x[:-1] for x in lines]


def part_one():
    pairslist = [x.split(',') for x in inputlist]
    pairslist = [[i.split('-') for i in x] for x in pairslist]
    pairslist = [[[int(i) for i in j] for j in x] for x in pairslist]
    pairslist = [(x[0][0] <= x[1][0] and x[0][1] >= x[1][1]) or (
        x[0][0] >= x[1][0] and x[0][1] <= x[1][1]) for x in pairslist]
    print('Part One: ', sum(pairslist))
