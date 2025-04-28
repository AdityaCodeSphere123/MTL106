def dp_row(p, q, N, array):
    numerator = 1
    denominator = 1
    array[0] = 1
    total_sum = 1
    for i in range(1, N+1):
        numerator *= p[i-1]
        denominator *= q[i]

        array[i] = numerator / denominator
        total_sum += array[i]
    
    return total_sum

def stationary_distribution(p, q, r, N):
    """
    Return a list of size N+1 containing the stationary distribution of the Markov chain.
    
    p : array of size N+1, 0 < p[i] < 1, probability of price increase
    q : array of size N+1, 0 < q[i] < 1, probability of price decrease
    r : array of size N+1, r[i] = 1 - p[i] - q[i], probability of price remaining the same
    N : int, the maximum price of the stock
    
    """
    stationary_state = [0] * (N+1)

    values = [0] * (N+1)
    total = 0

    total = dp_row(p, q, N, values)

    for j in range(N+1):
        stationary_state[j] = values[j] / total
    
    return stationary_state

def expected_wealth(p, q, r, N):
    """
    Return the expected wealth of the gambler in the long run.

    p : array of size N+1, 0 < p[i] < 1, probability of price increase
    q : array of size N+1, 0 < q[i] < 1, probability of price decrease
    r : array of size N+1, r[i] = 1 - p[i] - q[i], probability of price remaining the same
    N : int, the maximum price of the stock
    """
    stationary_state = [0] * (N+1)

    values = [0] * (N+1)
    total = 0

    total = dp_row(p, q, N, values)

    for j in range(N+1):
        stationary_state[j] = values[j] / total
    
    expected_price = 0

    for i in range(N+1):
        expected_price += (i * stationary_state[i])

    return expected_price

def get_coeff(p, q, r, N, a, b):

    coeff_E = [0 for _ in range(b)]
    const = [0 for _ in range(b)]

    coeff_E[0] = 1
    const[0] = 0

    coeff_E[1] = (1 - r[0]) / p[0]
    const[1] = (-1 / p[0])

    x = 2

    while(x < b):
        first_E = (1 - r[x-1]) * coeff_E[x-1]
        second_E = (q[x-1] * coeff_E[x-2])
        coeff_E[x] = (first_E - second_E) / p[x-1]

        first_const = (1 - r[x-1])* const[x-1]
        second_const = (q[x-1] * const[x-2]) + 1
        const[x] = (first_const - second_const) / p[x-1]

        x += 1

    return coeff_E, const


def expected_time(p, q, r, N, a, b):
    """
    Return the expected time for the price to reach b starting from a.

    p : array of size N+1, 0 < p[i] < 1, probability of price increase
    q : array of size N+1, 0 < q[i] < 1, probability of price decrease
    r : array of size N+1, r[i] = 1 - p[i] - q[i], probability of price remaining the same
    N : int, the maximum price of the stock
    a : int, the starting price
    b : int, the target price
    """

    coeff_E, const = get_coeff( p, q, r, N, a, b)

    numerator = 1 + (q[b-1] * const[b-2])
    numerator -= ((1 - r[b-1]) * const[b-1])

    denominator = ((1 - r[b-1]) * coeff_E[b-1])
    denominator -= (q[b-1] * coeff_E[b-2])

    expectation_0 = numerator / denominator

    return ((expectation_0 * coeff_E[a]) + const[a])