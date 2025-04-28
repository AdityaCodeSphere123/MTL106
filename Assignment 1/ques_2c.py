import numpy as np

class Alice:
    def __init__(self):
        self.past_play_styles = [1,1]
        self.results = [1,0]      
        self.opp_play_styles = [1,1]  
        self.points = 1

    def play_move(self):
        """
        Decide Alice's play style for the current round.
        
        Returns: 
            0 : attack
            1 : balanced
            2 : defence

        """
        if self.results[-1] == 1:
            total_game = len(self.results)
            pointA = self.points
            pointB = total_game - self.points
            x = (pointB / total_game)
            if x > (6 / 11):
                return 0
            else:
                return 2
            
        elif self.results[-1] == 0:
            return 1
        
        elif self.results[-1] == 0.5:
            return 0
        
    
    def observe_result(self, own_style, opp_style, result):
        """
        Update Alice's knowledge after each round based on the observed results.
        
        Returns:
            None
        """
        self.past_play_styles.append(own_style)
        self.results.append(result)
        self.opp_play_styles.append(opp_style)
        self.points += result
       

class Bob:
    def __init__(self):
        # Initialize numpy arrays to store Bob's past play styles, results, and opponent's play styles
        self.past_play_styles =[1,1] 
        self.results =[0,1]     
        self.opp_play_styles =[1,1]   
        self.points = 1

    def play_move(self):
        """
        Decide Bob's play style for the current round.

        Returns: 
            0 : attack
            1 : balanced
            2 : defence
        
        """
        if self.results[-1] == 1:
            return 2
        elif self.results[-1] == 0.5:
            return 1
        else:  
            return 0
        
        
        
    
    def observe_result(self, own_style, opp_style, result):
        """
        Update Bob's knowledge after each round based on the observed results.
        
        Returns:
            None
        """
        self.past_play_styles.append(own_style)
        self.results.append(result)
        self.opp_play_styles.append(opp_style)
        self.points += result
 

def simulate_round(alice, bob):
    """
    Simulates a single round of the game between Alice and Bob.
    
    Returns:
        None
    """
    play_alice = alice.play_move()
    play_bob = bob.play_move()

    alice_score = alice.points
    bob_score = bob.points
    
    payoff_matrix = np.array([
        [
            [(bob_score) / (alice_score + bob_score), 0, (alice_score) / (alice_score + bob_score)],
            [7 / 10, 0, 3 / 10],
            [5 / 11, 0, 6 / 11]
        ],
        [
            [3 / 10, 0, 7 / 10],
            [1/ 3, 1 / 3, 1 / 3],
            [3 / 10, 1 / 2, 1 / 5]
        ],
        [
            [6 / 11, 0, 5 / 11],
            [1 / 5, 1 / 2, 3 / 10],
            [1 / 10, 4 / 5, 1 / 10]
        ]
    ], dtype=float)

    final = np.random.choice(['alice_win', 'draw', 'bob_win'], p=payoff_matrix[play_alice][play_bob])

    if final == 'alice_win':
        alice_score = 1
        bob_score = 0
    elif final == 'draw':
        alice_score = 0.5
        bob_score = 0.5
    elif final == 'bob_win':
        bob_score = 1
        alice_score = 0
    
    alice.observe_result(play_alice, play_bob, alice_score)
    bob.observe_result(play_bob, play_alice, bob_score)

def estimate_tau(T):
    """
    Estimate the expected value of the number of rounds taken for Alice to win 'T' rounds.
    Your total number of simulations must not exceed 10^5.

    Returns:
        Float: estimated value of E[tau]
    """
    alice = Alice()
    bob = Bob()
    num_simulations = 100000
    final_list = []
    count = 0
    wins = 0


    for i in range(num_simulations):
        simulate_round(alice, bob)
        count += 1
        if alice.results[-1] == 1 :
            wins += 1
        if wins == T :
            final_list.append(count)
            wins = 0
            count = 0

    sum_list = sum(final_list)
    length = len(final_list)

    return sum_list/length

# print(estimate_tau(84))    
        
    