prev_line = None
amount = 0
with open('input.txt', 'r') as f:
    for line in f:
        if prev_line is not None and int(line) > prev_line:
            amount += 1
        prev_line = int(line)
print(amount)