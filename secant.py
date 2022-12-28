# DESCRIPTION:
# This algorithm finds a solution (x) for the equation f(x) = y using the secant method.
# It generally converges more quickly than the bisection method. 

# PARAMETERS: 
# y - Enter any real number you want
y = 15 # For example 15
# f(x) - Enter your function expression (must be a continuous function between x0 and x1)
f = lambda x : x**2 # For example, f(x) = x^2 so we want to solve x^2 = 15 (the square root of 15)

#-------- SECANT METHOD --------

g = lambda x : f(x) - y # We're going to solve g(x) = 0 (f(x) = y)
# Initialization of the sequence
x0 = 1
x1 = 8
x2 = x0 - g(x0)*(x1-x0)/(g(x1)-g(x0)) 


# Tolerance for the solution
eps = 0.001

# Max number of iterations in case it does not converge
MAX_ITERATIONS = 50
nb_iterations = 0

while not abs(g(x2)) < eps and nb_iterations < MAX_ITERATIONS:
    x2 = x0 - g(x0)*(x1-x0)/(g(x1)-g(x0)) 
    x0 = x1
    x1 = x2
    nb_iterations += 1
    
if nb_iterations == MAX_ITERATIONS:
    print("THE ALGORITHM DOES NOT CONVERGE TO A SOLUTION")
else:
    print(f"\nTHE ALGORITHM CONVERGES TO A SOLUTION ({nb_iterations} iterations) \nand the solution is: x = {x2} (tolerance = {eps})\n")
    










