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

def parse_equation(equation):
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

    reduced = "{} + {} * X^1 + {} * X^2 = 0".format(zero, one, two)
    degree = find_degree(zero, one, two)
    return reduced, degree

# def find_discriminant(equation):
# 	discriminant = 1
# 	return discriminant

def solve(equation):
	solution = 0
	return solution

def display(reduced, degree, solution):
    print("Reduced form: " + reduced)
    print("Polynomial degree: " + str(degree))

    # print("The solution is:")
    
    # print("Discriminant is strictly positive, the two solutions are:")
    # print(str(solution))

    # print("The polynomial degree is stricly greater than 2, I can't solve.")

def main():
    try:
        equation = parse_arg()
        reduced, degree = parse_equation(equation)
        solution = solve(reduced)
        ## discriminant = find_discriminant(reduced)
        display(reduced, degree, solution)
    except:
        print("Invalid Input")

if __name__ == '__main__':
    main()

## to run:
## python3 computor.py "5 * X^0 = 5 * X^0"
## python3 computor.py "$(< equations/0possible.txt)"