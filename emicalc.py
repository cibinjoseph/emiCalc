
# Set no. of iterations (a value greater than 10 is sufficient)
niter = 15

# Set initial approx. rate of interest (should be greater than 1.0)
xInitial = 1.30

def getA(P, r, n):
    """ Function to return amount """
    numer = P*r*(1.0+r)**n
    denom = ((1.0+r)**n)-1.0
    return numer/denom

def getr(P, A, n):
    """ Function to obtain rate of interest """
    x = xInitial
    # The following loop implements Newton's method of solving
    # non-linear equations
    for i in range(niter):
        # Uncomment the below line to print out intermmediate values
        # print(str(i) + "  " + str(x))
        numer = P*x**(n+1.0)-x**n*(A+P)+A
        denom = (n+1.0)*P*x**n-(A+P)*n*x**(n-1)
        x = x - numer/denom

    return x-1.0


# SAMPLE PROBLEM
P = 10000.0
r = 0.16
n = 2.0

# Finding amount from given values
A = getA(P, r, n)
print("Amount: " + str(A))

# Finding rate from P, A and n alone
rOut = getr(P, A, n)
print("Computed rate: " + str(rOut))
