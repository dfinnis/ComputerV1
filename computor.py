import argparse

def parse_args():
    my_parser = argparse.ArgumentParser(description="solves simple polynomial equations")
    my_parser.add_argument('Equation',
                       metavar='equation',
                       type=str,
                       help='provide a simple polynomial equation')
    my_parser.add_argument('-d',
                        '--decimal_places',
                        type=int,
                        help='set significant figures for displayed solution')
    my_parser.add_argument('-s',
                        '--steps',
                        action='store_true',
                        help='Display intermediate steps')
    args = my_parser.parse_args()
    equation = args.Equation
    decimal = args.decimal_places
    steps = args.steps
    return equation, decimal, steps

def parse_side(side):
    zero, one, two = 0, 0, 0
    for part in side:
        digit, Xpower = part.split("*")
        var, power = Xpower.split("^")
        power = float(power)
        if var != "X":
            print("Lexicon error. Variable not X:", var)
            sys.exit()
        if power == 0:
            zero += float(digit)
        elif power == 1:
            one += float(digit)
        elif power == 2:
            two += float(digit)
        else:
            print("The polynomial degree is stricly greater than 2, I can't solve. Power:", int(power))
            sys.exit()
    return(zero, one, two)

def find_degree(zero, one, two):
    if two == 0:
        if one == 0:
            return 0
        return 1
    else:
        return 2

def solve_zero(zero):
    if zero == 0:
        print("The solution is:\nAll real numbers")
    else:
        print("Equation unsolvable")

def solve_one(zero, one, decimal):
    solution = -zero/one
    if decimal != None:
        solution = "%.{}f".format(decimal) % solution
    print("The solution is:\n{}".format(solution))

def square_root(n):
    mn = 0
    mx = n if n >= 1 else 1
    while mx - mn > 0.000000001:
        mid = (mn + mx) / 2
        if mid * mid < n:
            mn = mid
        else:
            mx = mid
    return mx

def solve_two(zero, one, two, decimal):
    discriminant = one*one - 4*two*zero
    solution = -one / (2 * two)
    if discriminant < 0:
        sqrt = square_root(-discriminant) / (2 * two)
        if decimal != None:
            solution = "%.{}f".format(decimal) % solution
            sqrt = "%.{}f".format(decimal) % sqrt
        print("Discriminant is strictly negative, the two solutions are:")
        print("{} + i * {}\n{} - i * {}".format(solution, sqrt, solution, sqrt))
    elif discriminant == 0:
        if decimal != None:
            solution = "%.{}f".format(decimal) % solution
        print("Discriminant = 0, one double solution:", solution)
    else:
        sqrt = square_root(discriminant) / (2 * two)
        solution1 = solution + sqrt
        solution2 = solution - sqrt
        if decimal != None:
            solution1 = "%.{}f".format(decimal) % solution1
            solution2 = "%.{}f".format(decimal) % solution2
        print("Discriminant is strictly positive, the two solutions are:")    
        print("{}\n{}".format(solution1, solution2))

def print_steps(index, side, zeroS, oneS, twoS, zero, one, two, steps):
    if steps:
        print("side:", index + 1)
        print(side)
        print("-------------")
        print("side reduced")
        print("power zero:", zeroS)
        print("power one:", oneS)
        print("power two:", twoS)
        print("-------------")
        print("cumulative total")
        print("power zero:", zero)
        print("power one:", one)
        print("power two:", two)
        print("=============\n")

def solve(equation, decimal, steps):
    zero, one, two = 0, 0, 0
    if steps:
        print("\nEquation before parsing: {}\n".format(equation))
    equation = equation.replace(" ", "").replace("-", "+-").split("=")
    parts = [equation[i].split("+") for i in range(len(equation))]
    if len(parts) != 2:
        print("Syntax error. Number of '=':", len(parts) - 1)
        sys.exit()
    for index, side in enumerate(parts):
        zeroS, oneS, twoS = parse_side(side)
        if index == 0:
            zero += zeroS
            one += oneS
            two += twoS
        else:
            zero -= zeroS
            one -= oneS
            two -= twoS
        print_steps(index, side, zeroS, oneS, twoS, zero, one, two, steps)
    reduced = "{} + {} * X^1 + {} * X^2 = 0".format(zero, one, two)
    degree = find_degree(zero, one, two)
    print("Reduced form: " + reduced)
    print("Polynomial degree: " + str(degree))
    if degree == 0:
        solve_zero(zero)
    elif degree == 1:
        solve_one(zero, one, decimal)
    else:
        solve_two(zero, one, two, decimal)

def main():
    try:
        equation, decimal, steps = parse_args()
        solve(equation, decimal, steps)
    except:
        print("Invalid Input")

if __name__ == '__main__':
    main()

## to run:
## python3 computor.py "5 * X^0 = 5 * X^0"
## python3 computor.py "$(< equations/0possible.txt)"