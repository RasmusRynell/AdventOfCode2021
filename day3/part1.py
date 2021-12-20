size_of_binary = 12
how_many_zeros = [0] * size_of_binary
how_many_ones = [0] * size_of_binary
with open('input.txt', 'r') as f:
    for line in f:
        for bit in range(size_of_binary):
            if line[bit] == '0':
                how_many_zeros[bit] += 1
            elif line[bit] == '1':
                how_many_ones[bit] += 1

gamma = ''.join([str(int(how_many_zeros[bit] < how_many_ones[bit])) for bit in range(size_of_binary)])
epsilon = ''.join([str(int(how_many_zeros[bit] > how_many_ones[bit])) for bit in range(size_of_binary)])
print(int(gamma, 2) * int(epsilon, 2))