with open('input.txt') as file:
    lines = file.readlines()
inputlist = [x[:-1] for x in lines]
inputlist = [x.split(',') for x in inputlist]
inputlist = [[i.split('-') for i in x] for x in inputlist]
inputlist = [[[int(i) for i in j] for j in x] for x in inputlist]


def part_one():
    pairslist = [(x[0][0] <= x[1][0] and x[0][1] >= x[1][1]) or (
        x[0][0] >= x[1][0] and x[0][1] <= x[1][1]) for x in inputlist]
    print('Part One: ', sum(pairslist))


def part_two():
    pairslist = [(x[0][0] <= x[1][0] <= x[0][1] or x[1][0]
                  <= x[0][0] <= x[1][1]) for x in inputlist]
    print('Part Two: ', sum(pairslist))


part_one()
part_two()
