from sympy import symbols, Eq, solve

def parse_file(filename):
    input_array = []
    with open(filename, 'r') as f:
        for line in f:
            left_side, right_side = line.split(' @ ')
            left_numbers = [int(x) for x in left_side.split(', ')]
            right_numbers = [int(x) for x in right_side.split(', ')]
            input_array.append(left_numbers[:2] + right_numbers[:2])
    return input_array

def find_intersection(co_0, co_1):
    a0, c0, b0, d0 = co_0
    a1, c1, b1, d1 = co_1
    t1, t2 = symbols('t1 t2')

    x1 = a0 + b0*t1
    y1 = c0 + d0*t1
    x2 = a1 + b1*t2
    y2 = c1 + d1*t2
    
    eq1 = Eq(x1, x2)
    eq2 = Eq(y1, y2)
    solution = solve((eq1, eq2), (t1, t2))
    
    if solution == [] or float(solution[t1]) < 0 or float(solution[t2]) < 0:
        return None
    
    x = x1.subs(t1, solution[t1])
    y = y1.subs(t1, solution[t1])

    return (float(x), float(y))

def part2():
    a0, a1, a2, b0, b1, b2, t, t1, t2, t3 = symbols('a0 a1 a2 b0 b1 b2 t t1 t2 t3')

    eq1 = Eq(a0 + b0*t1, 152594199160345 + 229*t1)
    eq2 = Eq(a1 + b1*t1, 147562599184759 + 220*t1)
    eq3 = Eq(a2 + b2*t1, 291883234654893 - 31*t1)

    eq4 = Eq(a0 + b0*t2, 181402578613976 + 179*t2)
    eq5 = Eq(a1 + b1*t2, 206158696386036 + 99*t2)
    eq6 = Eq(a2 + b2*t2, 294595238970734 - 32*t2)

    eq7 = Eq(a0 + b0*t3, 306345582484815 - 19*t3)
    eq8 = Eq(a1 + b1*t3, 290719456201785 - 64*t3)
    eq9 = Eq(a2 + b2*t3, 306246299945991 - 43*t3)

    solution = solve((eq1,eq2,eq3,eq4,eq5,eq6,eq7,eq8,eq9), (a0, a1, a2, b0, b1, b2, t1, t2, t3))

    return solution[0][0] + solution[0][1] + solution[0][2]

input = parse_file("day24_input.txt")

total = 0
pairs_examined = 0
unique_pairs = int((len(input))*(len(input) - 1) / 2)
for i in range(len(input)):
    for j in range(i+1, len(input)):
        co_0, co_1 = input[i], input[j]
        result = find_intersection(co_0, co_1)
        if result != None:
            x, y = result
            if 200000000000000 <= x <= 400000000000000 and 200000000000000 <= y <= 400000000000000:
                total += 1
        pairs_examined += 1
        print('pairs examined: ', pairs_examined, '/', unique_pairs)
print(total)

print(part2())