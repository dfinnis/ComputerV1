import argparse

# def error_exit(err_msg):
#     print('Error: {}' .format(err_msg))
#     sys.exit()

def parse_arg():
    my_parser = argparse.ArgumentParser(description="solves simple polynomial equations")
    my_parser.add_argument('Equation',
                       metavar='equation',
                       type=str,
                       help='provide a simple polynomial equation')
    args = my_parser.parse_args()
    equation = args.Equation
    return equation

def reduce(equation):
    reduced = equation##########
    # equation.split("=")
    equation = equation.replace(" ", "").replace("-", "+-").split("=")
    parts = [equation[i].split("+") for i in range(len(equation))]
    print("equation:")    
    print(equation)
    print("parts:")    
    print(parts)
    print("0:")
    print(equation[0])
    print("1:")
    print(equation[1])
    print("==============")
    zero = 0
    one = 0
    two = 0
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