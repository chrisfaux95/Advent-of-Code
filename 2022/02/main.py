with open('input.txt') as file:
    lines = file.readlines()
inputlist = [x[:-1] for x in lines]

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

def part_one():
    scores = [rps_results[x] for x in inputlist]
    totalscore = sum(scores)
    return totalscore

print(part_one())