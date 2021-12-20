pos_horizontal = 0
depth = 0
with open('input.txt', 'r') as f:
    for line in f:
        direction, amount = line.split()
        if direction == 'forward':
            pos_horizontal += int(amount)
        elif direction == 'up':
            depth -= int(amount)
        elif direction == 'down':
            depth += int(amount)

print(pos_horizontal * amount_vertical)