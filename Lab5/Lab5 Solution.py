# Lab5: Design software to calculate continued fractions for a real number and for a rational number.
# By Jacob Bollinger

def findContinuedFraction(a, b) :
    continuedFraction = ''
    searching = True
    while (searching) :
        integer = a // b
        a = a - integer * b
        a,b = b,a
        continuedFraction = continuedFraction + ' ' + str(integer)
        searching = (b != 0)
    return continuedFraction

def findRealContinuedFraction(r, steps):
    continuedFraction = ''
    for i in range(steps) :
        integer = int(r)
        r = r - integer
        r = 1 / r
        continuedFraction = continuedFraction + ' ' + str(integer)
        i = i - 1
    return continuedFraction

# Inputs
# Numerator
N1 = 13
# Denomenator
N2 = 7
# Real Number
R = 2 ** (1/3)
# How many times findRealContinuedFraction runs
STEPS = 10

# Outputs
# Continued fraction of N1 / N2
print ('Continued Fraction:', findContinuedFraction(N1, N2))
# Real Continued Fraction
print ('Real Continued Fraction:', findRealContinuedFraction(R, STEPS))