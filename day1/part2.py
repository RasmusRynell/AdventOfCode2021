all_lines = []
with open('input.txt', 'r') as f:
    for line in f:
        all_lines.append(int(line))

print( sum(
    sum(all_lines[i - 3 : i]) < sum(all_lines[i - 2 : i + 1])
    for i in range(3, len(all_lines))
))