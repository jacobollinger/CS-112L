# Lab4 
# By Jacob Bollinger and 

# Define variable
N = 8

# Create a function to test if number n is prime
def isPrime(n) :
    if n <= 3 :
        prime = (n > 1)
    elif (n % 2 == 0) or (n % 3 == 0) :
        prime = False
    else :
        factor = 5
        prime = True
        while prime and (factor ** 2 <= n) :
            prime = (n % factor != 0) and (n % (factor + 2) != 0)
            factor = factor + 6
    return prime

# Create a function to find k and m values
def solve(n) :
    searching = True
    k = 1
    while searching and k < n :
        m = n - k
        searching = isPrime(2 ** k + m)
        if (searching) :
            k = k + 1
        else :
            searching = False
    return k, m

# Create a function that counts how many different k and m values there are
def counter(n) :
    k = 1
    count = 0
    for i in range (n) :
        k = i + 1
        m = n - k
        searching = isPrime(2 ** k + m)
        if (searching == False) :
            count = count + 1
    return count

print (N, 'is prime is', isPrime(N))
print ('k and m are', solve(N))
print ('There are', counter(N), 'solutions.')

# 