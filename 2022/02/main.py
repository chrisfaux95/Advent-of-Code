with open('input.txt') as file:
    lines = file.readlines()
inputlist = [x[:-1] for x in lines]


def part_one():
    rps_results = {
        'A X': 4,
        'A Y': 8,
        'A Z': 3,
        'B X': 1,
        'B Y': 5,
        'B Z': 9,
        'C X': 7,
        'C Y': 2,
        'C Z': 6
    }
    scores = [rps_results[x] for x in inputlist]
    totalscore = sum(scores)
    return totalscore


def part_two():
    rps_results = {
        'A X': 3,
        'A Y': 4,
        'A Z': 8,
        'B X': 1,
        'B Y': 5,
        'B Z': 9,
        'C X': 2,
        'C Y': 6,
        'C Z': 7
    }
    return sum([rps_results[x] for x in inputlist])

print(part_one())
print(part_two())
