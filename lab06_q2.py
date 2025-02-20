import random

class Rock_paper_scissors:
    def __init__(self, num_rounds):
        self.num_rounds = num_rounds
        self.current_round = 0
        self.user_wins = 0
        self.computer_wins = 0

    def get_computer_choice(self):
        choices = ["rock", "paper", "scissors"]
        return random.choice(choices)

    def find_winner(self, user_choice, computer_choice):
        if user_choice == computer_choice:
            return "tie"
        elif (
            (user_choice == "rock" and computer_choice == "scissors")
            or (user_choice == "paper" and computer_choice == "rock")
            or (user_choice == "scissors" and computer_choice == "paper")
        ):
            self.user_wins += 1
            return "user"
        else:
            self.computer_wins += 1
            return "computer"

    def play_round(self, user_choice):
        if self.current_round >= self.num_rounds:
            return "Game over"

        computer_choice = self.get_computer_choice()
        winner = self.find_winner(user_choice, computer_choice)
        self.current_round += 1
        return winner, computer_choice

    def check_game_over(self):
        return self.current_round >= self.num_rounds

    def get_final_winner(self):
        if self.user_wins > self.computer_wins:
            return "user"
        elif self.computer_wins > self.user_wins:
            return "computer"
        else:
            return "tie"

    def get_scores(self):
        return self.user_wins, self.computer_wins

    def get_round_number(self):
      return self.current_round
      
game = Rock_paper_scissors(3)  # Play 3 rounds

while not game.check_game_over():
    user_input = input("Enter rock, paper, or scissors: ").lower()
    if user_input not in ["rock", "paper", "scissors"]:
        print("Invalid input. Please enter rock, paper, or scissors.")
        continue

    round_winner, computer_choice = game.play_round(user_input)
    print(f"Round {game.get_round_number()}:")
    print(f"  You chose: {user_input}")
    print(f"  Computer chose: {computer_choice}")

    if round_winner == "tie":
        print("  It's a tie!")
    else:
        print(f"  {round_winner.capitalize()} wins this round!")

    user_score, computer_score = game.get_scores()
    print(f"  Score: User {user_score}, Computer {computer_score}")
    print("-" * 20)

final_winner = game.get_final_winner()
print("Game Over!")
if final_winner == "tie":
    print("It's a tie!")
else:
    print(f"{final_winner.capitalize()} wins the game!")
    