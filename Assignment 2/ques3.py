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

# def transition_matrix(W, p, q):
#     matrix = np.zeros((W + 1, W + 1))

#     matrix[0][0] = 1
#     matrix[0][1] = -p

#     matrix[W][W] = 1
#     matrix[W][W-1] = -1
#     for i in range(1, W):
#         matrix[i][i + 1] = -p
#         matrix[i][i - 1] = -q
#         matrix[i][i] = 1

#     return matrix

# def linear(matrix, W):
#     vector = np.ones((W + 1, 1))
#     solution = np.linalg.solve(matrix, vector)
#     return solution

def game_duration(p, q, k, t, W):
    """
    Return the expected number of rounds the gambler will play before quitting.

    p : float, 0 < p < 1, probability of winning a round
    q : float, q = 1 - p, probability of losing a round
    k : int, starting wealth
    t : int, t < k, the gambler will quit if she reaches t
    W : int, the threshold on maximum wealth the gambler can reach
    
    """
    # if W == 0:
    #     return (k - t)
    # else:
    #     matrix = transition_matrix(W, p, q)
    #     solution = linear(matrix, W)
    
    # return (k - t) * solution[0][0]

    if W == 0:
        return float(k - t)
    
    if p == q:
        return float((k - t)*((2*W) + 1))
    
    ratio = (p / q)
    power = W + 1
    denominator = q - p
    numerator = (1 - (2*q*(ratio**(power))))

    return float((numerator / denominator)*(k - t))