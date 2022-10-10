
# Set no. of iterations
niter = 15

# Set initial approx. rate of interest (should be greater than 1.0)
xInitial = 1.10

def getA(P, r, n):
    """ Function to return amount """
    numer = P*r*(1.0+r)**n
    denom = ((1.0+r)**n)-1.0
    return numer/denom

def getr(P, A, n):
    """ Function to obtain rate of interest """
    x = xInitial
    for i in range(niter):
        # Uncomment this to print out intermmediate values
        # print(i, end="  ")
        # print(x)
        numer = P*x**(n+1.0)-x**n*(A+P)+A
        denom = (n+1.0)*P*x**n-(A+P)*n*x**(n-1)
        x = x - numer/denom

    return x-1.0

# Sample problem
P = 10000.0
r = 0.16
n = 2.0
A = getA(P, r, n)
print("Amount: " + str(A))

rOut = getr(P, A, n)
print("Computed rate: " + str(rOut))

