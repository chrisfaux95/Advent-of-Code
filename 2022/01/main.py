with open('input.txt') as file:
    lines = file.readlines()
l = [x[:-1] for x in lines]
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

print(part_one(l))

