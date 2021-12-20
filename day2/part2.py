pos_horizontal = 0
depth = 0
aim = 0
with open('input.txt', 'r') as f:
    for line in f:
        direction, amount = line.split()
        if direction == 'forward':
            pos_horizontal += int(amount)
            depth += aim * int(amount)
        elif direction == 'up':
            aim -= int(amount)
        elif direction == 'down':
            aim += int(amount)

print(pos_horizontal * depth)