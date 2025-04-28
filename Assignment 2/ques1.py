def win_probability(p, q, k, N):
    """
    Return the probability of winning a game of chance.
    
    p : float, 0 < p < 1, probability of winning a round
    q : float, q = 1 - p, probability of losing a round
    k : int, starting wealth
    N : int, maximum wealth
    """

    if p == q:
        prob = k / N

    else:
        ratio = q * (1 / p)
        numerator = 1 - pow(ratio, k)
        denominator = 1 - pow(ratio, N)
        prob = numerator / denominator

    return prob
    

def limit_win_probability(p, q, k):
    """
    Return the probability of winning when the maximum wealth is infinity.
    
    p : float, 0 < p < 1, probability of winning a round
    q : float, q = 1 - p, probability of losing a round
    k : int, starting wealth
    """

    prob = 0

    if p > q:
        ratio = q * (1 / p)
        prob = 1 - pow(ratio, k)
    elif p == q:
        prob = 0
    else:
        prob = 0
    
    return prob



def game_duration(p, q, k, N):
    """
    Return the expected number of rounds to either win or get ruined.
    
    p : float, 0 < p < 1, probability of winning a round
    q : float, q = 1 - p, probability of losing a round
    k : int, starting wealth
    """

    expectation = 0

    if p == q:
        expectation = k * (N - k)
    else:
        ratio = (q/p)
        first = 1 / (q - p)
        first *= k
        numerator = 1 - pow(ratio, k)
        denominator = 1 - pow(ratio, N)
        second = 1 / (q - p)
        second *= N
        second *= (numerator / denominator)
        expectation = first - second

    return expectation