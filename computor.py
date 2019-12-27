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
        print("The solution is: all real numbers")
    else:
        print("Equation unsolvable")

def solve_one(zero, one):
    print("The solution is: ", -zero/one)

def solve_two(equation):
    solution = 2#######
    discriminant = 42########
    print(solution)

def solve(equation):
    zero = 0
    one = 0
    two = 0
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

        print("side:")
        print(side)
        print("-------------")
        print(zero)
        print(one)
        print(two)
        print("-------------")
        print(zero_side)
        print(one_side)
        print(two_side)
        print("-------------")

    reduced = "{} + {} * X^1 + {} * X^2 = 0".format(zero, one, two)
    degree = find_degree(zero, one, two)
    print("Reduced form: " + reduced)
    print("Polynomial degree: " + str(degree))
    if degree == 0:
        solve_zero(zero)
    elif degree == 1:
        solve_one(zero, one)
    else:
        solve_two(reduced)


# def find_discriminant(equation):
# 	discriminant = 1
# 	return discriminant


# def display(reduced, degree, solution, discriminant):
#     print("Reduced form: " + reduced)
#     print("Polynomial degree: " + str(degree))

#     print("The solution is:")
    
    # print("Discriminant is strictly positive, the two solutions are:")
    # print(str(solution))

    # print("The polynomial degree is stricly greater than 2, I can't solve.")

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