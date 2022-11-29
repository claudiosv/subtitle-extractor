def part1(lines):
    increases = 0
    for i in range(1, len(lines)):
        if int(lines[i]) > int(lines[i-1]):
            increases += 1
    print(increases)



with open('day1.txt', 'r') as f:
    lines_r = f.readlines()
    lines = list(map(int, lines_r))
    increases = 0
    sums =[] 
    for i in range(1, len(lines)-1):
        sum_3 = lines[i-1] + lines[i] + lines[i+1]
        print(sum_3)
        sums.append(sum_3)
    part1(sums)

def part1(lines):
    increases = 0
    for i in range(1, len(lines)):
        if int(lines[i]) > int(lines[i-1]):
            increases += 1
    print(increases)


