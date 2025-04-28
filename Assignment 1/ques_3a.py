import numpy as np

class Alice:
    def __init__(self):
        self.past_play_styles = [1,1]  
        self.results = [1,0]          
        self.opp_play_styles = [1,1] 
        self.points = 1

    def play_move(self):
        """
        Decide Alice's play style for the current round. Implement your strategy for 2a here.
         
        Returns: 
            0 : attack
            1 : balanced
            2 : defence

        """
        total_game = len(self.results)
        pointA = self.points
        pointB = total_game - self.points
        x = (pointB / total_game)
        if x > (15 / 44):
            
            return 0
        else:
            return 2
        
    
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
        self.past_play_styles = [1,1]  
        self.results = [1,0]          
        self.opp_play_styles = [1,1] 
        self.points = 1

    def play_move(self):
        """
        Decide Bob's play style for the current round.

        Returns: 
            0 : attack
            1 : balanced
            2 : defence
        
        """
        move = np.random.choice([0, 1, 2])
        return move
        
        
    
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
 

def simulate_round(alice, bob, payoff_matrix):
    """
    Simulates a single round of the game between Alice and Bob.
    
    Returns:
        None
    """
    alice_move = alice.play_move()
    bob_move = bob.play_move()
    
    result = np.random.choice(['alice_win', 'draw', 'bob_win'], p=payoff_matrix[alice_move][bob_move])

    # Assigning scores
    if result == 'alice_win':
        alice_score = 1
        bob_score = 0
    elif result == 'draw':
        alice_score = 0.5
        bob_score = 0.5
    elif result == 'bob_win':
        bob_score = 1
        alice_score = 0
    
    alice.observe_result(alice_move, bob_move, alice_score)
    bob.observe_result(bob_move, alice_move, bob_score)
    
    
def monte_carlo(num_rounds):
    """
    Runs a Monte Carlo simulation of the game for a specified number of rounds.
    
    Returns:
        None
    """
    alice = Alice()
    bob = Bob()
    # Payoff matrix
    payoff_matrix = np.array([
        [
            [1 / 2, 0, 1 / 2],
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

    for i in range(num_rounds):
        simulate_round(alice, bob, payoff_matrix)

        alice_score = alice.points
        bob_score = bob.points
        payoff_matrix[0][0][0] = (bob_score) / (alice_score + bob_score)
        payoff_matrix[0][0][2] = (alice_score) / (alice_score + bob_score)
        
    # print(f"Alice: {alice.points}")
    # print(f"Bob: {bob.points}")    
 

# Run Monte Carlo simulation with a specified number of rounds
if __name__ == "__main__":
    monte_carlo(num_rounds = 998)