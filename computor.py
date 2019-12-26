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
            sys.exit("Wrong power")########?????????
    return(zero, one, two)

def reduce(equation):
    zero = 0
    one = 0
    two = 0
    reduced = equation##########
    equation = equation.replace(" ", "").replace("-", "+-").split("=")
    parts = [equation[i].split("+") for i in range(len(equation))]
    if len(parts) != 2:
        sys.exit()
    print("equation:")    
    print(equation)
    print("parts:")    
    print(parts)
    print("0:")
    print(equation[0])
    print("1:")
    print(equation[1])
    print("==============")

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
        print(zero_side)
        print(one_side)
        print(two_side)
        print("-------------")

        print(zero)
        print(one)
        print(two)
        print("-------------")


    return reduced

def find_degree(equation):
	degree = 0
	return degree

# def find_discriminant(equation):
# 	discriminant = 1
# 	return discriminant

def solve(equation):
	solution = 0
	return solution

def display(equation, degree, solution):
    print("Reduced form: " + str(equation))
    # print(equation)
    print("Polynomial degree: " + str(degree))

    print("The solution is:")
    
    print("Discriminant is strictly positive, the two solutions are:")
    print(str(solution))

    print("The polynomial degree is stricly greater than 2, I can't solve.")

def main():
    print("oh hi")#####
    try:
        equation = parse_arg()
        reduced = reduce(equation)
        degree = find_degree(reduced)
        solution = solve(reduced)
        ## discriminant = find_discriminant(reduced)
        display(reduced, degree, solution)
    except:
        print("Invalid Input")
    print("bye now")##

if __name__ == '__main__':
    main()

## to run:
## python3 computor.py "5 * X^0 = 5 * X^0"
## python3 computor.py "$(< equations/0possible.txt)"