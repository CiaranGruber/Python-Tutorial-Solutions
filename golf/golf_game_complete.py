"""
Basic 2D Golf Game with a single 200m track.

Golf Game. 16/06/2020 - Created by Ciaran Gruber
"""

from golf.utilities import display_menu
from golf.utilities import get_max_length
import random

STARTING_DISTANCE = 230
HIT_INACCURACY = 0.2
CLUB_AND_DISTANCE = [("Driver", 100), ("Iron", 30), ("Putter", 10)]
PAR = 5
SCORE_TO_GOLF_TERM = {1: "Ace", PAR - 3: "Albatross", PAR - 2: "Eagle", PAR - 1: "Birdie", PAR: "Par", PAR + 1: "Bogey",
                      PAR + 2: "Double Bogey"}
VOWELS = ["A", "E", "I", "O", "U"]


def play_game() -> int:
    distance = STARTING_DISTANCE
    score = 0
    print("Welcome to the game of golf")
    while distance != 0:
        print("You are {}m away after {} shot{}.".format(distance, score, "s" if score != 1 else ""))

        # This uses shorthand list notation in python which can be quite powerful to allow to get certain elements
        # This code goes through each item in CLUB_AND_DISTANCE, gets the first element and returns it as a list
        club_choice = display_menu("Clubs:", [club_option[0] for club_option in CLUB_AND_DISTANCE], "Choose club: ",
                                   "Club choice must be an integer", "Club choice must be valid") - 1
        # If club is the one with the smallest distance (eg. Putter), set the club_distance to the remaining distance
        if CLUB_AND_DISTANCE[club_choice][1] == get_min_club()[1]:
            club_distance = distance
        else:
            club_distance = CLUB_AND_DISTANCE[club_choice][1]  # Get the club's average distance
        # Get the change of the distance due to HIT_INACCURACY (can be + or - to the distance)
        random_modifier = random.randint(int(-club_distance * HIT_INACCURACY), int(club_distance * HIT_INACCURACY))
        if club_distance - random_modifier < 0:  # Distance can't be < 0
            shot_distance = 0
        else:
            shot_distance = club_distance + random_modifier
        print("\nYour shot went {}m".format(shot_distance))
        distance = abs(distance - shot_distance)
        score += 1
    endgame_message = "Clunk... After {} shots, the ball is in the hole ".format(score)
    if score < PAR:
        endgame_message += "Congratulations! "
    elif score == PAR:
        endgame_message += "Good job. "
    else:
        endgame_message += "Disappointing. "
    endgame_message += "Your final score was "
    if score in SCORE_TO_GOLF_TERM:
        golf_term = SCORE_TO_GOLF_TERM[score]
        endgame_message += "an" if golf_term[0].upper() in VOWELS else "a"  # Basic check whether to put an or a
        endgame_message += " {}.".format(golf_term)
    else:
        # The "%+d" % (shots - PAR) includes the + or - sign at the front
        endgame_message += str("%+d" % (score - PAR))
    print(endgame_message)
    return score


def get_min_club() -> tuple:
    """Get the tuple representing the club that travels the least distance"""
    min_club_index = 0
    min_club_distance = float('inf')
    for i, club in enumerate(CLUB_AND_DISTANCE):
        if club[1] < min_club_distance:
            min_club_index = i
    return CLUB_AND_DISTANCE[min_club_index]


def show_instructions():
    """Show the instructions for the golf game"""
    instructions = "This is a simple golf game in which each hole is {}m game away with par {}.".format(
        STARTING_DISTANCE, PAR)
    instructions += "\nYou are able to choose the following clubs:"
    for club, distance in CLUB_AND_DISTANCE:
        instructions += "\n\t- {} ({}m)".format(club, distance)
    instructions += "\nEach club has an inaccuracy of {:.0f}% of its total".format(HIT_INACCURACY * 100)
    instructions += "\nThe {} will decrease its distance if you are within its max distance to the hole".format(
        get_min_club()[0])
    print(instructions)


def show_statistics(stats: list):
    """Print the golf game statistics"""
    print("Statistics:")
    max_round_length = len(str(len(stats)))
    max_shot_length = get_max_length(stats)
    for round_number, shots in enumerate(stats):
        statistic_string = "Round {:>{}} : ".format(round_number + 1, max_round_length)
        statistic_string += "{:>{}} shots. ".format(shots, max_shot_length)
        # Return the correct golf term or by default just display points relative to par
        # The "%+d" % (shots - PAR) includes the + or - sign at the front
        statistic_string += "{}.".format(SCORE_TO_GOLF_TERM.get(shots, "%+d" % (shots - PAR)))
        print(statistic_string)


def main():
    """Run the game of golf"""
    menu_option = 0
    stats = []
    print("Welcome to Ciaran's Golf Game")
    while menu_option != 4:
        menu_option = display_menu("Menu:", ["Play", "Instructions", "Statistics", "Quit"], "Menu choice: ",
                                   "Menu choice must be an integer\n", "Menu choice must be 1-4\n")
        print()
        if menu_option == 1:
            stats.append(play_game())
        elif menu_option == 2:
            show_instructions()
        elif menu_option == 3:
            show_statistics(stats)
        if menu_option != 4:  # You don't want a double space after the quit message, this just ensures that
            print()
    print("See you. Hope you had fun")


if __name__ == "__main__":
    main()
