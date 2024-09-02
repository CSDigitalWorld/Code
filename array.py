import array

# Remember array indeces start from (0) and go until (array_size - 1)

# Set up an array with initial scores for 5 players
player_scores = array.array('i', [0, 0, 0, 0, 0])

# Simulate updating scores
player_scores[1] = 15  # Player 2 scores 15 points
player_scores[4] = 22  # Player 5 scores 22 points

# Add a new score for an additional player (expanding array)
player_scores.append(30)  # New player scores 30 points

# Remove the score of Player 3 (index 2)
del player_scores[2]

# Print the updated scoreboard
print("Updated Player Scores:", player_scores)
