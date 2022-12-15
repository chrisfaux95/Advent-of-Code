with open('input.txt') as file:
    packet = file.read()


def part_one():
    result = 0
    for i in range(len(packet)):
        x = set(packet[i:i+4])
        if len(x) > 3:
            result = i+4
            break
    print('Part One: ', result)


part_one()
