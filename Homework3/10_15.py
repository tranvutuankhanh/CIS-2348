# Name: Vu Tran
# Student ID: 2233511

# Define a class called Team
class Team:
    def __init__(self, team_name='none', team_wins=0, team_losses=0):
        # Initialize instance variables for team name, number of wins, and number of losses
        self.team_name = team_name
        self.team_wins = team_wins
        self.team_losses = team_losses

    # Define a method to calculate the win percentage
    def get_win_percentage(self):
        return self.team_wins / (self.team_wins + self.team_losses)


# If this file is being run as the main program
if __name__ == "__main__":
    # Prompt the user for the team name, number of wins, and number of losses
    team_name = input()
    team_wins = int(input())
    team_losses = int(input())

    # Create a new instance of the Team class with the user input values
    team = Team(team_name, team_wins, team_losses)

    # If the team's win percentage is greater than or equal to 0.5
    if team.get_win_percentage() >= 0.5:
        # Print a congratulatory message
        print('Congratulations, Team', team.team_name, 'has a winning average!')
    else:
        # Otherwise, print a message indicating the team has a losing average
        print('Team', team.team_name, 'has a losing average.')
