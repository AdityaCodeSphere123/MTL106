from fractions import Fraction
"""
Use the following functions to add, multiply and divide, taking care of the modulo operation.
Use mod_add to add two numbers taking modulo 1000000007. ex : c=a+b --> c=mod_add(a,b)
Use mod_multiply to multiply two numbers taking modulo 1000000007. ex : c=a*b --> c=mod_multiply(a,b)
Use mod_divide to divide two numbers taking modulo 1000000007. ex : c=a/b --> c=mod_divide(a,b)
"""
M=1000000007

def mod_add(a, b):
    a=(a%M+M)%M
    b=(b%M+M)%M
    return (a+b)%M

def mod_multiply(a, b):
    a=(a%M+M)%M
    b=(b%M+M)%M
    return (a*b)%M

def mod_divide(a, b):
    a=(a%M+M)%M
    b=(b%M+M)%M
    return mod_multiply(a, pow(b, M-2, M))

# Problem 1a
def calc_prob(alice_wins, bob_wins):
    """
    Returns:
        The probability of Alice winning alice_wins times and Bob winning bob_wins times will be of the form p/q,
        where p and q are positive integers,
        return p.q^(-1) mod 1000000007.
    """
    # Assigning values for Alice wins and Bob wins
    nA = alice_wins
    nB = bob_wins
    prob = []

    # Taking the maximum value of nA and nB
    n = max(nA, nB)

    # Initializing all values to 0 of the 2D grid
    prob = [[Fraction(0, 1) for _ in range(n)] for _ in range(n)]

    # Base Case
    prob[0][0] = Fraction(1, 1)

    # Assigning values to the x and y axis
    for i in range(1, n):
        prob[0][i] = prob[0][i-1] * Fraction(1, i+1)
        prob[i][0] = prob[0][i]
    
    # Recursive equation
    for x in range(1, n):
        for y in range(1, n):
            prob[x][y] = prob[x-1][y] * Fraction(y + 1, x + y + 1) + prob[x][y-1] * Fraction(x + 1, x + y + 1)
    
    # Returning the answer
    answer = mod_divide(prob[nA-1][nB-1].numerator, prob[nA-1][nB-1].denominator)
    return answer
    
# Problem 1b (Expectation)      
def calc_expectation(t):
    """
    Returns:
        The expected value of \sum_{i=1}^{t} Xi will be of the form p/q,
        where p and q are positive integers,
        return p.q^(-1) mod 1000000007.
    """
    # Creating same matrix as above
    prob = [] 

    prob = [[Fraction(0, 1) for _ in range(t)] for _ in range(t)]
    prob[0][0] = Fraction(1, 1)

    for i in range(1, t):
        prob[0][i] = prob[0][i-1] * Fraction(1, i+1)
        prob[i][0] = prob[0][i]
    
    for x in range(1, t):
        for y in range(1, t):
            prob[x][y] = prob[x-1][y] * Fraction(y + 1, x + y + 1) + prob[x][y-1] * Fraction(x + 1, x + y + 1)

    # calculating expectation
    Expectation = 0
    # y is rv of summation Xi
    # Its value ranges from -(n-2) to n-2
    for y in range(-(t-2), (t-1)):

        # This condition from solving (done in theory)
        if ((y+t) % 2) == 0:
            Expectation += y * prob[(t+y)//2 - 1][t - ((t+y)//2) - 1]
    
    # Returning answer
    answer = mod_divide(Expectation.numerator, Expectation.denominator)
    return answer

# Problem 1b (Variance)
def calc_variance(t):
    """
    Returns:
        The variance of \sum_{i=1}^{t} Xi will be of the form p/q,
        where p and q are positive integers,
        return p.q^(-1) mod 1000000007.

    """
    # Creating 2D matrix as before
    prob = [] 
    prob = [[Fraction(0, 1) for _ in range(t)] for _ in range(t)]

    prob[0][0] = Fraction(1, 1)

    for i in range(1, t):
        prob[0][i] = prob[0][i-1] * Fraction(1, i+1)
        prob[i][0] = prob[0][i]
    
    for x in range(1, t):
        for y in range(1, t):
            prob[x][y] = prob[x-1][y] * Fraction(y + 1, x + y + 1) + prob[x][y-1] * Fraction(x + 1, x + y + 1)

    # Calculating variance
    Variance = 0

    for y in range(-(t-2), (t-1), 2):

        Variance += y * y * prob[(t+y)//2 - 1][t - ((t+y)//2) - 1]
    
    # Returning answer
    answer = mod_divide(Variance.numerator, Variance.denominator)
    return answer

# T1T2 = 92
# T3T4 = 84
# print(calc_expectation(T3T4))
# print(calc_variance(T3T4))
# print(calc_prob(T1T2, T3T4))