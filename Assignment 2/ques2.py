"""
Use the following function to convert the decimal fraction of k/N into it's binary representation
using k_prec number of bits after the decimal point. You may assume that the expansion of 
k/N terminates before k_prec bits after the decimal point.
"""
def decimalToBinary(num, k_prec) : 
  
    binary = ""  
    Integral = int(num)    
    fractional = num - Integral 
   
    while (Integral) :       
        rem = Integral % 2
        binary += str(rem);  
        Integral //= 2

    binary = binary[ : : -1]  
    binary += '.'

    while (k_prec) : 
        fractional *= 2
        fract_bit = int(fractional)  
  
        if (fract_bit == 1) :  
            fractional -= fract_bit  
            binary += '1'       
        else : 
            binary += '0'
        k_prec -= 1
        
    return binary     

def decimal_from_bin_string(bin_str):
    if "." in bin_str :
        before_dec, _, after_dec = bin_str.partition('.')

    int_part = int(before_dec,2) if before_dec != "" else 0
    frac_part = sum(int(bit) * 0.5 ** position for position, bit in enumerate(after_dec, start=1))

    return int_part + frac_part

def prob_recur(p,q,k,N):
    fin = 0
    if k == 0 :
        fin =  0
    elif k == N :
        fin =  1
    elif k == N/2 :
        fin =  p
    elif k > N/2 :
        fin =  p + (q * win_probability(p,q,(2*k)-N,N))
    elif k < N/2 :
        fin =  (p * win_probability(p,q,2*k,N))
    
    return fin
    
def exp_recur(p,q,k,N):
    fin = 0
    if k == 0 or k == N :
        fin =  0
    elif k >= N/2 :
        fin =  1 + (q * game_duration(p,q,(2*k)-N,N))
    elif k < N/2 :
        fin =  1 + (p * game_duration(p,q,(2*k),N))

    return fin

def win_probability(p, q, k, N):
    """
    Return the probability of winning while gambling aggressively.
    
    p : float, 0 < p < 1, probability of winning a round
    q : float, q = 1 - p, probability of losing a round
    k : int, starting wealth
    N : int, maximum wealth
    """
    resultant = k/N
    binary_string = decimalToBinary(resultant, 50)
    resultant_new = decimal_from_bin_string(binary_string)
    k = resultant_new * N
    final_prob = prob_recur(p,q,k,N)
    return final_prob


def game_duration(p, q, k, N):
    """
    Return the expected number of rounds to either win or get ruined while gambling aggressively.
    
    p : float, 0 < p < 1, probability of winning a round
    q : float, q = 1 - p, probability of losing a round
    k : int, starting wealth
    N : int, maximum wealth
    """
    resultant = k/N
    binary_string = decimalToBinary(resultant, 50)
    resultant_new = decimal_from_bin_string(binary_string)
    k = resultant_new*N
    final_exp = exp_recur(p,q,k,N)
    return final_exp