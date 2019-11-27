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
	reduced = equation
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
        ## find discriminant
        display(reduced, degree, solution)
    except:
        print("Invalid Input")
    print("bye now")##

if __name__ == '__main__':
    main()

## to run:
## python3 computor.py "$(< equations/0possible.txt)"