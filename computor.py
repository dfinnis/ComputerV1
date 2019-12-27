import argparse

def parse_arg():
    my_parser = argparse.ArgumentParser(description="solves simple polynomial equations")
    my_parser.add_argument('Equation',
                       metavar='equation',
                       type=str,
                       help='provide a simple polynomial equation')
    args = my_parser.parse_args()
    equation = args.Equation
    return equation

def parse_side(side):
    zero, one, two = 0, 0, 0
    for part in side:
        # if part == "":
        #     continue
        digit, Xpower = part.split("*")
        var, power = Xpower.split("^")
        power = float(power)
        if var != "X":
            sys.exit()
        if power == 0:
            zero += float(digit)
        elif power == 1:
            one += float(digit)
        elif power == 2:
            two += float(digit)
        else:
            print("The polynomial degree is stricly greater than 2, I can't solve.")
            sys.exit()
    return(zero, one, two)

def find_degree(zero, one, two):
    if two == 0 and one == 0:
        return 0
    elif two == 0:
        return 1
    else:
        return 2

def solve_zero(zero):
    if zero == 0:
        print("The solution is:\nAll real numbers")
    else:
        print("Equation unsolvable")

def solve_one(zero, one):
    print("The solution is:\n{}".format(-zero/one))

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

def solve_two(zero, one, two):
    discriminant = one*one - 4*two*zero
    solution = -one / (2 * two)
    if discriminant < 0:
        sqrt = square_root(-discriminant) / (2 * two)
        print("Discriminant is strictly negative, the two solutions are:")
        print("{} + i * {}\n{} - i * {}".format(solution, sqrt, solution, sqrt))
    elif discriminant == 0:
        print("Discriminant = 0, one double solution:", solution)
    else:
        sqrt = square_root(discriminant) / (2 * two)
        print("Discriminant is strictly positive, the two solutions are:")
        print("{}\n{}".format(solution + sqrt, solution - sqrt))

def solve(equation):
    zero, one, two = 0, 0, 0
    equation = equation.replace(" ", "").replace("-", "+-").split("=")
    parts = [equation[i].split("+") for i in range(len(equation))]
    if len(parts) != 2:
        sys.exit()
    for index, side in enumerate(parts):
        zero_side, one_side, two_side = parse_side(side)
        if index == 0:
            zero += zero_side
            one += one_side
            two += two_side
        else:
            zero -= zero_side
            one -= one_side
            two -= two_side

        # print("side: {}".format(index))
        # print(side)
        # print("-------------")
        # print(zero)
        # print(one)
        # print(two)
        # print("-------------")
        # print(zero_side)
        # print(one_side)
        # print(two_side)
        # print("-------------")

    reduced = "{} + {} * X^1 + {} * X^2 = 0".format(zero, one, two)
    degree = find_degree(zero, one, two)
    print("Reduced form: " + reduced)
    print("Polynomial degree: " + str(degree))
    if degree == 0:
        solve_zero(zero)
    elif degree == 1:
        solve_one(zero, one)
    else:
        solve_two(zero, one, two)

def main():
    try:
        equation = parse_arg()
        solve(equation)
    except:
        print("Invalid Input")

if __name__ == '__main__':
    main()

## to run:
## python3 computor.py "5 * X^0 = 5 * X^0"
## python3 computor.py "$(< equations/0possible.txt)"